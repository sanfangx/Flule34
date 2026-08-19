import 'package:flutter/foundation.dart';

/// Hanime1 评论（来源：`loadComment` 返回的 HTML 片段）。
@immutable
final class HanimeComment {
  const HanimeComment({
    required this.id,
    required this.username,
    required this.content,
    this.avatarUrl,
    this.dateLabel,
    this.likeCount = 0,
    this.replyCount = 0,
    this.isReply = false,
    this.liked = false,
    this.disliked = false,
    this.likesCount = 0,
    this.likesSum = 0,
    this.reportableType = 'comment',
  });

  final String id;
  final String username;
  final String content;
  final String? avatarUrl;
  final String? dateLabel;
  final int likeCount;
  final int replyCount;
  final bool isReply;
  final bool liked;
  final bool disliked;
  final int likesCount;
  final int likesSum;
  final String reportableType;
}
