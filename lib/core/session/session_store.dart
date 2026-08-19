import 'dart:async';

import 'package:cookie_jar/cookie_jar.dart';
import 'package:flutter/foundation.dart';

import '../database/app_database.dart';
import '../logging/app_log_service.dart';
import 'secret_store.dart';

@immutable
final class SessionUser {
  const SessionUser({required this.id});

  final String id;
}

@immutable
final class StoredCredentials {
  const StoredCredentials({required this.email, required this.password});

  final String email;
  final String password;
}

class SessionStore extends ChangeNotifier {
  SessionStore({
    required this.cookieJar,
    required this.secretStore,
    required this.database,
  });

  static const _userIdKey = 'flule34.session.user_id';
  static const _emailKey = 'flule34.session.email';
  static const _passwordKey = 'flule34.session.password';
  static const _hanimeUserIdKey = 'flule34.session.hanime1.user_id';
  static const _hanimeEmailKey = 'flule34.session.hanime1.email';
  static const _hanimePasswordKey = 'flule34.session.hanime1.password';
  static final _validUserId = RegExp(r'^\d+$');

  final PersistCookieJar cookieJar;
  final SecretStore secretStore;
  final AppDatabase database;

  SessionUser? _currentUser;
  SessionUser? _currentHanimeUser;
  bool _loaded = false;

  SessionUser? get currentUser => _currentUser;
  String? get currentUserId => _currentUser?.id;
  bool get isLoggedIn => _currentUser != null;
  SessionUser? get hanimeUser => _currentHanimeUser;
  String? get hanimeUserId => _currentHanimeUser?.id;
  bool get isHanimeLoggedIn => _currentHanimeUser != null;
  bool get isLoaded => _loaded;

  Future<void> load() async {
    try {
      await cookieJar.forceInit();
      final storedUserId = await secretStore.read(_userIdKey);
      if (storedUserId != null && _validUserId.hasMatch(storedUserId)) {
        _currentUser = SessionUser(id: storedUserId);
        await database.recordAuthenticatedAccount(storedUserId);
      }
    } on Object catch (error, stackTrace) {
      _currentUser = null;
      unawaited(
        AppLogService.instance.error(
          error,
          stackTrace,
          component: 'session_load',
        ),
      );
    }
    try {
      final storedHanimeUserId = await secretStore.read(_hanimeUserIdKey);
      if (storedHanimeUserId != null &&
          _validUserId.hasMatch(storedHanimeUserId)) {
        _currentHanimeUser = SessionUser(id: storedHanimeUserId);
      }
    } on Object catch (error, stackTrace) {
      _currentHanimeUser = null;
      unawaited(
        AppLogService.instance.error(
          error,
          stackTrace,
          component: 'session_load_hanime',
        ),
      );
    }
    _loaded = true;
    notifyListeners();
  }

  Future<void> authenticate(String userId) async {
    final normalized = userId.trim();
    if (!_validUserId.hasMatch(normalized)) {
      throw ArgumentError.value(userId, 'userId', '用户 ID 格式无效');
    }

    final previousUserId = await secretStore.read(_userIdKey);
    try {
      await secretStore.write(_userIdKey, normalized);
      await database.recordAuthenticatedAccount(normalized);
    } on Object {
      if (previousUserId == null) {
        await secretStore.delete(_userIdKey);
      } else {
        await secretStore.write(_userIdKey, previousUserId);
      }
      rethrow;
    }
    if (_currentUser?.id == normalized) {
      return;
    }
    _currentUser = SessionUser(id: normalized);
    notifyListeners();
  }

  Future<String?> cookieHeaderFor(Uri uri) async {
    final cookies = await cookieJar.loadForRequest(uri);
    if (cookies.isEmpty) {
      return null;
    }
    return cookies.map(_cookiePair).join('; ');
  }

  Future<void> authenticateHanime(String userId) async {
    final normalized = userId.trim();
    if (!_validUserId.hasMatch(normalized)) {
      throw ArgumentError.value(userId, 'userId', '用户 ID 格式无效');
    }

    final previousUserId = await secretStore.read(_hanimeUserIdKey);
    try {
      await secretStore.write(_hanimeUserIdKey, normalized);
    } on Object {
      if (previousUserId == null) {
        await secretStore.delete(_hanimeUserIdKey);
      } else {
        await secretStore.write(_hanimeUserIdKey, previousUserId);
      }
      rethrow;
    }
    if (_currentHanimeUser?.id == normalized) {
      return;
    }
    _currentHanimeUser = SessionUser(id: normalized);
    notifyListeners();
  }

  Future<StoredCredentials?> loadHanimeCredentials() async {
    final values = await Future.wait([
      secretStore.read(_hanimeEmailKey),
      secretStore.read(_hanimePasswordKey),
    ]);
    final email = values[0]?.trim() ?? '';
    final password = values[1] ?? '';
    if (email.isEmpty || password.isEmpty) {
      return null;
    }
    return StoredCredentials(email: email, password: password);
  }

  Future<void> saveHanimeCredentials({
    required String email,
    required String password,
  }) async {
    final normalizedEmail = email.trim();
    if (normalizedEmail.isEmpty || password.isEmpty) {
      throw ArgumentError('账号和密码不能为空。');
    }
    await Future.wait([
      secretStore.write(_hanimeEmailKey, normalizedEmail),
      secretStore.write(_hanimePasswordKey, password),
    ]);
  }

  Future<void> forgetHanimeCredentials() async {
    await Future.wait([
      secretStore.delete(_hanimeEmailKey),
      secretStore.delete(_hanimePasswordKey),
    ]);
  }

  Future<void> clearHanime({bool forgetCredentials = false}) async {
    await Future.wait([
      secretStore.delete(_hanimeUserIdKey),
      if (forgetCredentials) secretStore.delete(_hanimeEmailKey),
      if (forgetCredentials) secretStore.delete(_hanimePasswordKey),
    ]);
    if (_currentHanimeUser == null) {
      return;
    }
    _currentHanimeUser = null;
    notifyListeners();
  }

  Future<StoredCredentials?> loadCredentials() async {
    final values = await Future.wait([
      secretStore.read(_emailKey),
      secretStore.read(_passwordKey),
    ]);
    final email = values[0]?.trim() ?? '';
    final password = values[1] ?? '';
    if (email.isEmpty || password.isEmpty) {
      return null;
    }
    return StoredCredentials(email: email, password: password);
  }

  Future<void> saveCredentials({
    required String email,
    required String password,
  }) async {
    final normalizedEmail = email.trim();
    if (normalizedEmail.isEmpty || password.isEmpty) {
      throw ArgumentError('账号和密码不能为空。');
    }
    await Future.wait([
      secretStore.write(_emailKey, normalizedEmail),
      secretStore.write(_passwordKey, password),
    ]);
  }

  Future<void> clearCookies() => cookieJar.deleteAll();

  Future<void> clearCookiesFor(Uri uri) => cookieJar.delete(uri, true);

  Future<void> clear({bool forgetCredentials = false, Uri? cookieScope}) async {
    await Future.wait([
      cookieScope == null
          ? cookieJar.deleteAll()
          : cookieJar.delete(cookieScope, true),
      secretStore.delete(_userIdKey),
      if (forgetCredentials) secretStore.delete(_emailKey),
      if (forgetCredentials) secretStore.delete(_passwordKey),
    ]);
    if (_currentUser == null) {
      return;
    }
    _currentUser = null;
    notifyListeners();
  }

  String _cookiePair(Cookie cookie) => '${cookie.name}=${cookie.value}';
}
