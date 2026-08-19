import 'package:flutter/foundation.dart';

/// Rule34Video 评论（来源：详情页 `#video_comments_video_comments_items`
/// 服务端渲染的评论项；该站无回复、无赞踩）。
@immutable
final class Rule34VideoComment {
  const Rule34VideoComment({
    required this.id,
    required this.username,
    required this.content,
    this.avatarUrl,
    this.dateLabel,
  });

  final String id;
  final String username;
  final String content;
  final String? avatarUrl;
  final String? dateLabel;
}
