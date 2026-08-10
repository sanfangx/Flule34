import 'package:flutter/services.dart';
import 'package:google_mlkit_language_id/google_mlkit_language_id.dart';

import '../models/translation_models.dart';

abstract interface class SourceLanguageDetector {
  Future<TranslationLanguage?> detect(String text);

  Future<void> dispose();
}

final class MlKitSourceLanguageDetector implements SourceLanguageDetector {
  MlKitSourceLanguageDetector({double confidenceThreshold = 0.8})
    : _identifier = LanguageIdentifier(
        confidenceThreshold: confidenceThreshold,
      );

  final LanguageIdentifier _identifier;

  @override
  Future<TranslationLanguage?> detect(String text) async {
    final normalized = text.trim();
    if (normalized.isEmpty || _hasMixedScripts(normalized)) return null;
    final code = await _identifier.identifyLanguage(normalized);
    if (code == 'und') return null;
    return TranslationLanguage.fromCodeOrNull(code);
  }

  @override
  Future<void> dispose() async {
    try {
      await _identifier.close();
    } on MissingPluginException {
      // Flutter 单元测试没有 ML Kit 平台通道，真机不会进入此分支。
    }
  }

  static bool _hasMixedScripts(String text) {
    final hasLatin = RegExp(r'[A-Za-z]').hasMatch(text);
    final hasKana = RegExp(r'[\u3040-\u30ff]').hasMatch(text);
    final hasHangul = RegExp(r'[\uac00-\ud7af]').hasMatch(text);
    final hasHan = RegExp(r'[\u3400-\u9fff]').hasMatch(text);

    if (hasLatin && (hasKana || hasHangul || hasHan)) return true;
    if (hasHangul && (hasKana || hasHan)) return true;
    // 日语通常同时使用假名与汉字，应作为同一种文字系统处理。
    return hasKana && hasHangul;
  }
}
