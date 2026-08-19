import 'package:flutter/foundation.dart';

@immutable
final class MemberProfile {
  const MemberProfile({
    required this.id,
    required this.displayName,
    this.avatarUrl,
    this.subscribersLabel,
    this.coverUrl,
    this.verified = false,
    this.details = const {},
  });

  final String id;
  final String displayName;
  final String? avatarUrl;
  final String? subscribersLabel;
  final String? coverUrl;
  final bool verified;
  final Map<String, String> details;
}

/// Hanime1 站点的账号信息（来源：首页 `#user-modal-*` 区块）。
@immutable
final class HanimeAccountProfile {
  const HanimeAccountProfile({
    required this.id,
    required this.displayName,
    this.avatarUrl,
    this.subscriberCount,
    this.videoCount,
  });

  final String id;
  final String displayName;
  final String? avatarUrl;
  final int? subscriberCount;
  final int? videoCount;
}

@immutable
final class HanimeAccountEditData {
  const HanimeAccountEditData({
    required this.token,
    required this.name,
    required this.email,
    this.avatarUrl,
  });

  final String token;
  final String name;
  final String email;
  final String? avatarUrl;
}
