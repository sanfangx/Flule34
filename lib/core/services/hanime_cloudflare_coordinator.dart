import 'dart:async';
import 'dart:collection';

import 'package:flutter/foundation.dart';

final class HanimeCloudflareRequest {
  const HanimeCloudflareRequest({
    required this.id,
    required this.targetUri,
    required this.allowForegroundVerification,
  });

  final int id;
  final Uri targetUri;
  final bool allowForegroundVerification;
}

bool canCompleteHanimeBrowserPage({
  required bool isTargetHost,
  required bool isChallenge,
  required bool hasDocument,
  required int progress,
  required String readyState,
  required bool observedChallenge,
  required bool hasClearance,
}) {
  if (!isTargetHost || isChallenge || !hasDocument) return false;
  final isLoaded = progress >= 90 || (hasClearance && readyState == 'complete');
  if (!isLoaded) return false;
  return !observedChallenge || hasClearance;
}

final class HanimeCloudflareCoordinator extends ChangeNotifier {
  HanimeCloudflareRequest? _activeRequest;
  final ListQueue<_PendingBrowserPage> _queue = ListQueue();
  final Map<String, _PendingBrowserPage> _pendingByUrl = {};
  var _nextId = 0;
  int? _foregroundRequestId;

  HanimeCloudflareRequest? get activeRequest => _activeRequest;
  bool get requiresForeground =>
      _activeRequest != null && _activeRequest!.id == _foregroundRequestId;

  Future<String?> requestPage(
    Uri targetUri, [
    bool allowForegroundVerification = true,
  ]) {
    final key = '${targetUri.toString()}#$allowForegroundVerification';
    final existing = _pendingByUrl[key];
    if (existing != null) return existing.completer.future;

    final pending = _PendingBrowserPage(
      request: HanimeCloudflareRequest(
        id: ++_nextId,
        targetUri: targetUri,
        allowForegroundVerification: allowForegroundVerification,
      ),
      completer: Completer<String?>(),
    );
    _pendingByUrl[key] = pending;
    _queue.add(pending);
    _activateNext();
    return pending.completer.future;
  }

  void complete({required int requestId, String? html}) {
    final request = _activeRequest;
    if (request == null || request.id != requestId || _queue.isEmpty) {
      return;
    }
    final pending = _queue.removeFirst();
    if (pending.request.id != requestId) return;

    _pendingByUrl.remove(
      '${pending.request.targetUri}#${pending.request.allowForegroundVerification}',
    );
    _activeRequest = null;
    _foregroundRequestId = null;
    if (!pending.completer.isCompleted) pending.completer.complete(html);
    _activateNext(notify: false);
    notifyListeners();
  }

  void requestForeground({required int requestId}) {
    final request = _activeRequest;
    if (request?.id != requestId || _foregroundRequestId == requestId) {
      return;
    }
    if (!request!.allowForegroundVerification) {
      complete(requestId: requestId);
      return;
    }
    _foregroundRequestId = requestId;
    notifyListeners();
  }

  void _activateNext({bool notify = true}) {
    if (_activeRequest != null || _queue.isEmpty) return;
    _activeRequest = _queue.first.request;
    if (notify) notifyListeners();
  }

  @override
  void dispose() {
    for (final pending in _queue) {
      if (!pending.completer.isCompleted) pending.completer.complete(null);
    }
    _queue.clear();
    _pendingByUrl.clear();
    _activeRequest = null;
    _foregroundRequestId = null;
    super.dispose();
  }
}

final class _PendingBrowserPage {
  const _PendingBrowserPage({required this.request, required this.completer});

  final HanimeCloudflareRequest request;
  final Completer<String?> completer;
}
