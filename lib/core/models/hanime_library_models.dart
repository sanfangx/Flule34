import 'package:flutter/foundation.dart';

import 'video_models.dart';

enum HanimeHistorySort {
  latest('latest', '最新'),
  popular('popular', '热门'),
  oldest('oldest', '最早');

  const HanimeHistorySort(this.queryValue, this.label);

  final String queryValue;
  final String label;
}

@immutable
final class HanimeSubscriptionArtist {
  const HanimeSubscriptionArtist({required this.name, this.avatarUrl});

  final String name;
  final String? avatarUrl;
}

@immutable
final class HanimeSubscriptionPage {
  const HanimeSubscriptionPage({
    this.artists = const [],
    this.videos = const [],
  });

  final List<HanimeSubscriptionArtist> artists;
  final List<VideoItem> videos;
}
