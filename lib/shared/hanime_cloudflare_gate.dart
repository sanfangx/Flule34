import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../app/providers.dart';
import '../features/home/hanime_cloudflare_page.dart';

/// 全局 Cloudflare 验证弹窗。
///
/// 需要浏览器辅助验证时（[HanimeCloudflareCoordinator.activeRequest] 非空），
/// 在整屏上方叠加半透明遮罩 + 居中卡片式验证弹窗；验证完成或取消后自动
/// 移除，主界面恢复。
final class HanimeCloudflareGate extends ConsumerWidget {
  const HanimeCloudflareGate({super.key, required this.child});

  final Widget child;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final coordinator = ref.watch(hanimeCloudflareCoordinatorProvider);
    final api = ref.watch(rule34VideoApiProvider).hanime1Api;
    return ListenableBuilder(
      listenable: coordinator,
      builder: (context, _) {
        final request = coordinator.activeRequest;
        return PopScope(
          canPop: request == null,
          onPopInvokedWithResult: (didPop, _) {
            if (!didPop && request != null) {
              coordinator.complete(requestId: request.id);
            }
          },
          child: Stack(
            fit: StackFit.expand,
            children: [
              child,
              if (request != null) ...[
                const Positioned.fill(
                  child: AbsorbPointer(
                    child: ColoredBox(color: Colors.black45),
                  ),
                ),
                HanimeCloudflarePage(
                  key: ValueKey(request.id),
                  api: api,
                  targetUri: request.targetUri,
                  onPageReady: (html) =>
                      coordinator.complete(requestId: request.id, html: html),
                  onCancel: () => coordinator.complete(requestId: request.id),
                ),
              ],
            ],
          ),
        );
      },
    );
  }
}
