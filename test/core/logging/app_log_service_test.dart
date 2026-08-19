import 'dart:io';

import 'package:flutter_test/flutter_test.dart';

import 'package:flule34/core/logging/app_log_service.dart';
import 'package:flule34/core/security/error_redaction.dart';

void main() {
  test('Hanime 用户路径和用户字段会被脱敏', () {
    final result = redactSensitiveText(
      'GET /user/123456/playlists；用户=PrivateName；userId=123456',
    );
    expect(result, isNot(contains('123456')));
    expect(result, isNot(contains('PrivateName')));
    expect(result, contains('/user/<redacted>/playlists'));
  });

  test('日志导出文件名精确到分钟', () {
    expect(
      logExportFileName(DateTime(2026, 8, 10, 20, 6, 59)),
      'HaRu-logs-202608102006.txt',
    );
  });

  test('日志自动脱敏、按七天保留并支持清除', () async {
    final root = await Directory.systemTemp.createTemp('flule34-app-log-');
    addTearDown(() async {
      if (await root.exists()) {
        await root.delete(recursive: true);
      }
    });
    final now = DateTime(2026, 8, 7, 12);
    final directory = Directory(
      '${root.path}${Platform.pathSeparator}flule34_logs',
    )..createSync(recursive: true);
    await File(
      '${directory.path}${Platform.pathSeparator}flule34-2026-07-31.log',
    ).writeAsString('old');
    final service = AppLogService.forTesting(
      supportDirectory: () async => root,
      clock: () => now,
    );

    await service.initialize();
    await service.error(
      StateError('password=secret-value'),
      StackTrace.current,
      component: 'test',
    );

    final text = await service.readAll();
    expect(text, contains('[ERROR] [test]'));
    expect(text, isNot(contains('secret-value')));
    expect(
      await File(
        '${directory.path}${Platform.pathSeparator}flule34-2026-07-31.log',
      ).exists(),
      isFalse,
    );
    expect((await service.storageInfo()).fileCount, 1);

    await service.clear();
    expect((await service.storageInfo()).fileCount, 0);
  });

  test('错误日志会保留足够长的调用栈用于符号化', () async {
    final root = await Directory.systemTemp.createTemp('flule34-stack-log-');
    addTearDown(() async {
      if (await root.exists()) {
        await root.delete(recursive: true);
      }
    });
    final service = AppLogService.forTesting(
      supportDirectory: () async => root,
      clock: () => DateTime(2026, 8, 8, 12),
    );
    await service.initialize();
    final stack = StackTrace.fromString(
      '${List.generate(180, (index) => '#$index frame-$index').join('\n')}\n'
      'tail-symbolization-marker',
    );
    await service.error(
      StateError('player failure'),
      stack,
      component: 'video',
    );

    final text = await service.readAll();
    expect(text, contains('tail-symbolization-marker'));
    expect(text, contains('\n#1 frame-1'));
    expect(text, isNot(contains(r'\n#1 frame-1')));
    expect(text.length, greaterThan(2000));
  });
}
