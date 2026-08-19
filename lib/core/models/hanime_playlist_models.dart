import 'package:flutter/foundation.dart';

/// Hanime1 播放列表条目（来源：`user/{id}/playlists` 页面卡片）。
@immutable
final class HanimePlaylist {
  const HanimePlaylist({
    required this.listCode,
    required this.title,
    this.videoCount,
    this.coverUrl,
    this.description = '',
  });

  final String listCode;
  final String title;
  final int? videoCount;
  final String? coverUrl;
  final String description;
}
