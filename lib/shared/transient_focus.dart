import 'package:flutter/material.dart';

void dismissInputFocus() {
  FocusManager.instance.primaryFocus?.unfocus();
}

Future<T?> runWithoutRestoringInputFocus<T>(
  BuildContext context,
  Future<T?> Function() showTransientUi,
) async {
  dismissInputFocus();
  final result = await showTransientUi();
  if (context.mounted) {
    FocusScope.of(context).unfocus();
    WidgetsBinding.instance.addPostFrameCallback((_) => dismissInputFocus());
  }
  return result;
}
