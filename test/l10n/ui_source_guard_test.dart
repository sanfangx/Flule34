import 'dart:io';

import 'package:flutter_test/flutter_test.dart';

void main() {
  test('用户可见中文不得绕过 AppText 或 context.uiText', () {
    final unsafeTab = RegExp(r'''\bTab\s*\(\s*text\s*:''');
    final han = RegExp(r'[\u3400-\u9fff]');
    final kindLabel = RegExp(r'(?:\bkind|\.kind)\.label');
    final findings = <String>[];
    for (final entity in Directory('lib').listSync(recursive: true)) {
      if (entity is! File || !entity.path.endsWith('.dart')) continue;
      final path = entity.path.replaceAll('\\', '/');
      if (path.contains('/l10n/generated/') ||
          path.endsWith('/l10n/ui_translations.g.dart')) {
        continue;
      }
      final source = entity.readAsStringSync();
      for (final invocation in _plainTextInvocations(source)) {
        final explicitlyLocalized = invocation.source.contains(
          'context.uiText(',
        );
        if (!explicitlyLocalized &&
            (han.hasMatch(invocation.source) ||
                kindLabel.hasMatch(invocation.source))) {
          findings.add(
            '$path:${_lineAt(source, invocation.offset)} '
            'unlocalized ${invocation.widget}',
          );
        }
      }
      for (final match in unsafeTab.allMatches(source)) {
        findings.add('$path:${_lineAt(source, match.start)} Tab.text');
      }
    }
    expect(findings, isEmpty, reason: findings.join('\n'));
  });
}

int _lineAt(String source, int offset) =>
    '\n'.allMatches(source.substring(0, offset)).length + 1;

Iterable<_Invocation> _plainTextInvocations(String source) sync* {
  final starts = RegExp(r'\b(Text|SelectableText)\s*\(').allMatches(source);
  for (final start in starts) {
    final open = source.indexOf('(', start.start);
    final end = _matchingParenthesis(source, open);
    if (end == null) continue;
    yield _Invocation(
      widget: start.group(1)!,
      offset: start.start,
      source: source.substring(start.start, end + 1),
    );
  }
}

int? _matchingParenthesis(String source, int open) {
  var depth = 0;
  String? quote;
  var escaped = false;
  for (var index = open; index < source.length; index += 1) {
    final character = source[index];
    if (quote != null) {
      if (escaped) {
        escaped = false;
      } else if (character == r'\') {
        escaped = true;
      } else if (character == quote) {
        quote = null;
      }
      continue;
    }
    if (character == "'" || character == '"') {
      quote = character;
    } else if (character == '(') {
      depth += 1;
    } else if (character == ')' && --depth == 0) {
      return index;
    }
  }
  return null;
}

final class _Invocation {
  const _Invocation({
    required this.widget,
    required this.offset,
    required this.source,
  });

  final String widget;
  final int offset;
  final String source;
}
