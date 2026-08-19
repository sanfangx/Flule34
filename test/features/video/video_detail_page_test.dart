import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:video_player_platform_interface/video_player_platform_interface.dart';

import 'package:flule34/app/providers.dart';
import 'package:flule34/core/api/rule34video_api.dart';
import 'package:flule34/core/models/video_models.dart';
import 'package:flule34/core/session/session_store.dart';
import 'package:flule34/core/services/network_status_service.dart';
import 'package:flule34/core/services/screen_wake_lock_service.dart';
import 'package:flule34/features/downloads/domain/download_models.dart';
import 'package:flule34/features/settings/data/app_settings_store.dart';
import 'package:flule34/features/video/video_detail_page.dart';
import 'package:flule34/features/video/video_player_page.dart';

import '../../helpers/test_session_harness.dart';

void main() {
  test('全屏内部路由不会触发详情页暂停策略', () {
    expect(shouldPauseVideoForRoutePush(true), isFalse);
    expect(shouldPauseVideoForRoutePush(false), isTrue);
  });

  testWidgets('播放时锁定播放器，明确暂停后才可上推并固定详情页签', (tester) async {
    final originalPlatform = VideoPlayerPlatform.instance;
    final platform = _FakeVideoPlayerPlatform();
    VideoPlayerPlatform.instance = platform;
    addTearDown(() async {
      VideoPlayerPlatform.instance = originalPlatform;
      await platform.close();
    });
    final harness = TestSessionHarness.create();
    addTearDown(harness.dispose);
    await harness.sessionStore.load();
    await harness.sessionStore.authenticate('1001');
    final api = _FakeVideoApi(harness.sessionStore);
    final playerHandle = VideoPlayerHandle();
    addTearDown(playerHandle.dispose);
    final container = ProviderContainer(
      overrides: [
        rule34VideoApiProvider.overrideWithValue(api),
        appDatabaseProvider.overrideWithValue(harness.database),
        appSettingsStoreProvider.overrideWithValue(_MemorySettingsStore()),
        downloadPlatformServiceProvider.overrideWithValue(
          _FakeDownloadPlatformService(),
        ),
        networkStatusServiceProvider.overrideWithValue(
          _FakeNetworkStatusService(),
        ),
        screenWakeLockServiceProvider.overrideWithValue(
          _FakeScreenWakeLockService(),
        ),
      ],
    );
    addTearDown(container.dispose);

    await tester.pumpWidget(
      UncontrolledProviderScope(
        container: container,
        child: MaterialApp(
          home: VideoDetailPage(
            api: api,
            video: _video,
            playerHandle: playerHandle,
          ),
        ),
      ),
    );
    addTearDown(() async {
      await tester.pumpWidget(const SizedBox.shrink());
      await tester.pump();
    });
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 300));
    playerHandle.debugSetPlaybackState(playing: true, buffering: false);
    await tester.pump();
    expect(playerHandle.canCollapseDetails, isFalse);

    expect(find.text('喜欢'), findsNothing);
    expect(find.text('不喜欢'), findsNothing);
    expect(find.text('播放列表'), findsOneWidget);
    expect(find.text('本地分类库'), findsOneWidget);
    expect(find.text('3D · ↑12 ↓3'), findsOneWidget);
    // 新布局：简介|评论 Tab（rule34video 评论 Tab 为占位，无真实输入框）。
    expect(find.text('简介'), findsOneWidget);
    expect(find.text('评论'), findsOneWidget);
    expect(find.text('新增一则公开评论...'), findsNothing);
    expect(find.text('播放'), findsNothing);
    final playerFinder = find.byKey(
      const ValueKey('video-detail-player-region'),
    );
    expect(playerFinder, findsOneWidget);
    final playerTop = tester.getTopLeft(playerFinder).dy;
    final nestedState = tester.state<NestedScrollViewState>(
      find.byType(NestedScrollView),
    );
    expect(
      find.byWidgetPredicate(
        (widget) =>
            widget is NotificationListener<OverscrollIndicatorNotification>,
      ),
      findsOneWidget,
    );
    final innerScrollable = find.descendant(
      of: find.byType(ListView),
      matching: find.byType(Scrollable),
    );
    final innerPosition = tester
        .state<ScrollableState>(innerScrollable)
        .position;

    final playingGesture = await tester.startGesture(
      tester.getCenter(find.byType(ListView)),
    );
    for (var index = 0; index < 6; index += 1) {
      await playingGesture.moveBy(const Offset(0, -100));
      await tester.pump(const Duration(milliseconds: 16));
      expect(nestedState.outerController.offset, closeTo(0, 0.01));
      expect(tester.getTopLeft(playerFinder).dy, closeTo(playerTop, 0.1));
    }
    await playingGesture.up();
    await tester.pumpAndSettle();
    expect(nestedState.outerController.offset, closeTo(0, 0.01));
    expect(tester.getTopLeft(playerFinder).dy, closeTo(playerTop, 0.1));

    final reverseGesture = await tester.startGesture(
      tester.getCenter(find.byType(ListView)),
    );
    for (var index = 0; index < 3; index += 1) {
      await reverseGesture.moveBy(const Offset(0, 60));
      await tester.pump(const Duration(milliseconds: 16));
      expect(nestedState.outerController.offset, closeTo(0, 0.01));
      expect(tester.getTopLeft(playerFinder).dy, closeTo(playerTop, 0.1));
    }
    await reverseGesture.up();
    await tester.pumpAndSettle();
    expect(nestedState.outerController.offset, closeTo(0, 0.01));
    expect(tester.getTopLeft(playerFinder).dy, closeTo(playerTop, 0.1));
    final innerBeforePause = innerPosition.pixels;
    expect(innerBeforePause, greaterThan(0));

    playerHandle.debugSetPlaybackState(playing: false, buffering: false);
    await tester.pump();
    expect(playerHandle.canCollapseDetails, isTrue);
    expect(nestedState.outerController.offset, closeTo(0, 0.01));
    expect(innerPosition.pixels, closeTo(innerBeforePause, 0.01));

    await tester.fling(find.byType(ListView), const Offset(0, -1200), 3000);
    await tester.pumpAndSettle();
    expect(nestedState.outerController.offset, greaterThan(0));
    final innerBeforeResume = innerPosition.pixels;
    expect(innerBeforeResume, greaterThanOrEqualTo(0));
    expect(tester.getTopLeft(find.text('简介')).dy, greaterThanOrEqualTo(0));

    playerHandle.debugSetPlaybackState(playing: true, buffering: false);
    await tester.pump();
    expect(nestedState.outerController.offset, greaterThan(0));
    expect(innerPosition.pixels, closeTo(innerBeforeResume, 0.01));
    final outerSamples = <double>[];
    for (var index = 0; index < 5; index += 1) {
      await tester.pump(const Duration(milliseconds: 50));
      outerSamples.add(nestedState.outerController.offset);
      expect(innerPosition.pixels, closeTo(innerBeforeResume, 0.01));
    }
    expect(
      outerSamples,
      contains(isNot(nestedState.outerController.position.maxScrollExtent)),
    );
    await tester.pumpAndSettle();
    expect(nestedState.outerController.offset, closeTo(0, 0.01));
    expect(innerPosition.pixels, closeTo(innerBeforeResume, 0.01));
    expect(tester.getTopLeft(playerFinder).dy, closeTo(playerTop, 0.1));
  });

  testWidgets('视频详情加载失败后可原位重试且不会因重建重复请求', (tester) async {
    final harness = TestSessionHarness.create();
    addTearDown(harness.dispose);
    await harness.sessionStore.load();
    final api = _RetryVideoApi(harness.sessionStore);
    final container = ProviderContainer(
      overrides: [
        appDatabaseProvider.overrideWithValue(harness.database),
        appSettingsStoreProvider.overrideWithValue(_MemorySettingsStore()),
        downloadPlatformServiceProvider.overrideWithValue(
          _FakeDownloadPlatformService(),
        ),
      ],
    );
    addTearDown(container.dispose);

    await tester.pumpWidget(
      UncontrolledProviderScope(
        container: container,
        child: MaterialApp(
          home: VideoDetailPage(api: api, video: _video),
        ),
      ),
    );
    await tester.pumpAndSettle();

    expect(find.text('详情暂时不可用'), findsOneWidget);
    expect(api.detailLoads, 1);
    await tester.pump();
    expect(api.detailLoads, 1);

    await tester.tap(find.text('重试'));
    await tester.pumpAndSettle();

    expect(find.text('测试视频'), findsOneWidget);
    expect(find.text('此视频未提供可直接播放的 MP4 源。'), findsOneWidget);
    expect(api.detailLoads, 2);
  });

  testWidgets('超长分类标签卡片会自动换行而不是截断', (tester) async {
    final harness = TestSessionHarness.create();
    addTearDown(harness.dispose);
    await harness.sessionStore.load();
    final api = _LongMetadataApi(harness.sessionStore);
    final container = ProviderContainer(
      overrides: [
        appDatabaseProvider.overrideWithValue(harness.database),
        appSettingsStoreProvider.overrideWithValue(_MemorySettingsStore()),
        downloadPlatformServiceProvider.overrideWithValue(
          _FakeDownloadPlatformService(),
        ),
      ],
    );
    addTearDown(container.dispose);

    await tester.pumpWidget(
      UncontrolledProviderScope(
        container: container,
        child: MaterialApp(
          home: VideoDetailPage(api: api, video: _video),
        ),
      ),
    );
    await tester.pumpAndSettle();

    final label = 'very-long-bilingual-tag-that-must-wrap-on-a-phone-screen';
    final labelFinder = find.text(label);
    expect(labelFinder, findsOneWidget);
    expect(tester.getSize(labelFinder).height, greaterThan(20));
  });

  testWidgets('长按详情页标题行的文字外空白处也可打开标题编辑', (tester) async {
    final harness = TestSessionHarness.create();
    addTearDown(harness.dispose);
    await harness.sessionStore.load();
    final api = _FakeVideoApi(harness.sessionStore);
    final container = ProviderContainer(
      overrides: [
        appDatabaseProvider.overrideWithValue(harness.database),
        appSettingsStoreProvider.overrideWithValue(_MemorySettingsStore()),
        downloadPlatformServiceProvider.overrideWithValue(
          _FakeDownloadPlatformService(),
        ),
      ],
    );
    addTearDown(container.dispose);

    await tester.pumpWidget(
      UncontrolledProviderScope(
        container: container,
        child: MaterialApp(
          home: VideoDetailPage(api: api, video: _video),
        ),
      ),
    );
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 300));

    final region = find.byKey(
      const ValueKey('video-detail-title-translation-region'),
    );
    final rect = tester.getRect(region);
    expect(rect.width, greaterThan(tester.getSize(find.text('测试视频')).width));

    final gesture = await tester.startGesture(
      Offset(rect.right - 8, rect.center.dy),
    );
    await tester.pump(const Duration(milliseconds: 600));
    await gesture.up();
    await tester.pump(const Duration(milliseconds: 300));

    expect(find.text('编辑译文'), findsOneWidget);
    expect(find.byType(TextField), findsOneWidget);
  });
}

final class _FakeNetworkStatusService implements NetworkStatusService {
  @override
  Future<NetworkClass> current() async => NetworkClass.wifi;
}

final class _FakeScreenWakeLockService implements ScreenWakeLockService {
  @override
  Future<void> setEnabled(bool enabled) async {}
}

const _video = VideoItem(id: '123', title: '测试视频', slug: 'test-video');

const _details = VideoDetails(
  video: _video,
  sources: [],
  categories: ['3D'],
  tags: ['example'],
  models: ['Artist'],
  metadataItems: [
    VideoMetadataItem(
      id: '1',
      title: '3D',
      path: '/categories/1/3d/',
      kind: DiscoveryKind.category,
      upScore: 12,
      downScore: 3,
    ),
  ],
  isFavorite: false,
);

class _FakeVideoApi extends Rule34VideoApi {
  _FakeVideoApi(SessionStore sessionStore) : super(sessionStore: sessionStore);

  int detailLoads = 0;

  @override
  Future<VideoDetails> loadVideoDetails(VideoItem video) async {
    detailLoads += 1;
    return _details;
  }

  @override
  Future<List<SubscriptionItem>> loadSubscriptions({
    bool force = false,
  }) async => const [];

  @override
  void close() {}
}

class _RetryVideoApi extends Rule34VideoApi {
  _RetryVideoApi(SessionStore sessionStore) : super(sessionStore: sessionStore);

  int detailLoads = 0;

  @override
  Future<VideoDetails> loadVideoDetails(VideoItem video) async {
    detailLoads += 1;
    if (detailLoads == 1) {
      throw const ApiException('详情暂时不可用');
    }
    return const VideoDetails(
      video: _video,
      sources: [],
      categories: [],
      tags: [],
      models: [],
      isFavorite: false,
    );
  }

  @override
  void close() {}
}

class _LongMetadataApi extends Rule34VideoApi {
  _LongMetadataApi(SessionStore sessionStore)
    : super(sessionStore: sessionStore);

  @override
  Future<VideoDetails> loadVideoDetails(VideoItem video) async =>
      const VideoDetails(
        video: _video,
        sources: [],
        categories: [],
        tags: [],
        models: [],
        metadataItems: [
          VideoMetadataItem(
            id: 'long-tag',
            title: 'very-long-bilingual-tag-that-must-wrap-on-a-phone-screen',
            path: '/tags/long-tag/',
            kind: DiscoveryKind.tag,
            upScore: 0,
            downScore: 0,
          ),
        ],
        isFavorite: false,
      );

  @override
  void close() {}
}

final class _FakeVideoPlayerPlatform extends VideoPlayerPlatform {
  final StreamController<VideoEvent> _events =
      StreamController<VideoEvent>.broadcast();

  int playCount = 0;

  @override
  Future<void> init() async {}

  @override
  Future<int?> createWithOptions(VideoCreationOptions options) async {
    Timer.run(() {
      if (!_events.isClosed) {
        _events.add(
          VideoEvent(
            eventType: VideoEventType.initialized,
            duration: const Duration(minutes: 2),
            size: const Size(1280, 720),
          ),
        );
      }
    });
    return 1;
  }

  @override
  Stream<VideoEvent> videoEventsFor(int playerId) => _events.stream;

  @override
  Widget buildViewWithOptions(VideoViewOptions options) {
    return const ColoredBox(color: Colors.black);
  }

  @override
  Future<void> play(int playerId) async {
    playCount += 1;
    _events.add(
      VideoEvent(
        eventType: VideoEventType.isPlayingStateUpdate,
        isPlaying: true,
      ),
    );
  }

  @override
  Future<void> pause(int playerId) async {
    _events.add(
      VideoEvent(
        eventType: VideoEventType.isPlayingStateUpdate,
        isPlaying: false,
      ),
    );
  }

  @override
  Future<void> seekTo(int playerId, Duration value) async {}

  @override
  Future<Duration> getPosition(int playerId) async => Duration.zero;

  @override
  Future<void> setVolume(int playerId, double value) async {}

  @override
  Future<void> setPlaybackSpeed(int playerId, double value) async {}

  @override
  Future<void> setLooping(int playerId, bool looping) async {}

  @override
  Future<void> setMixWithOthers(bool mixWithOthers) async {}

  @override
  Future<void> setAllowBackgroundPlayback(bool allowBackgroundPlayback) async {}

  @override
  Future<void> dispose(int playerId) async {}

  Future<void> close() => _events.close();
}

final class _MemorySettingsStore implements AppSettingsStore {
  final Map<String, Object> _values = {};

  @override
  Future<bool?> readBool(String key) async => _values[key] as bool?;

  @override
  Future<String?> readString(String key) async => _values[key] as String?;

  @override
  Future<void> writeBool(String key, bool value) async {
    _values[key] = value;
  }

  @override
  Future<void> writeString(String key, String value) async {
    _values[key] = value;
  }

  @override
  Future<void> remove(String key) async {
    _values.remove(key);
  }
}

final class _FakeDownloadPlatformService implements DownloadPlatformService {
  @override
  Stream<DownloadPlatformEvent> get events => const Stream.empty();

  @override
  Future<bool> cancel(String taskId) async => true;

  @override
  Future<bool> pause(String taskId) async => true;

  @override
  Future<bool> resume(String taskId) async => true;

  @override
  Future<bool> delete({
    required String taskId,
    String? fileUri,
    bool deleteExternalFile = true,
  }) async => true;

  @override
  void dispose() {}

  @override
  Future<bool> taskExists(String taskId) async => false;

  @override
  Future<bool> enqueue(DownloadRequest request) async => true;

  @override
  Future<bool> ensureNotificationPermission() async => true;

  @override
  Future<bool> ensureSharedStoragePermission() async => true;

  @override
  Future<DownloadFileInspection> inspectFile(String fileUri) async =>
      const DownloadFileInspection(exists: true, readable: true);

  @override
  Future<void> initialize() async {}

  @override
  Future<void> setMaxConcurrent(int value) async {}

  @override
  Future<bool> openFile(String fileUri) async => true;
}
