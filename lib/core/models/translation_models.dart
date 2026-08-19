import 'package:flutter/foundation.dart';

enum TranslationLanguage {
  simplifiedChinese('简体中文', 'zh-Hans', 'ZH-HANS', 'zh-CN'),
  english('English', 'en', 'EN-US', 'en'),
  japanese('日本語', 'ja', 'JA', 'ja'),
  korean('한국어', 'ko', 'KO', 'ko');

  const TranslationLanguage(
    this.label,
    this.code,
    this.deepLCode,
    this.myMemoryCode,
  );

  final String label;
  final String code;
  final String deepLCode;
  final String myMemoryCode;

  static TranslationLanguage fromCode(
    String? code, {
    TranslationLanguage fallback = TranslationLanguage.english,
  }) {
    final normalized = code?.trim().toLowerCase().replaceAll('_', '-');
    return switch (normalized) {
      'zh' || 'zh-cn' || 'zh-hans' => simplifiedChinese,
      'en' || 'en-us' || 'en-gb' => english,
      'ja' || 'jp' => japanese,
      'ko' || 'kr' => korean,
      _ => fallback,
    };
  }

  static TranslationLanguage? fromCodeOrNull(String? code) {
    final normalized = code?.trim().toLowerCase().replaceAll('_', '-');
    return switch (normalized) {
      'zh' || 'zh-cn' || 'zh-hans' || 'zh-hant' || 'zh-tw' => simplifiedChinese,
      'en' || 'en-us' || 'en-gb' => english,
      'ja' || 'jp' => japanese,
      'ko' || 'kr' => korean,
      _ => null,
    };
  }
}

enum TranslationTargetPreference {
  followInterface('跟随界面语言'),
  simplifiedChinese('简体中文'),
  english('English'),
  japanese('日本語'),
  korean('한국어');

  const TranslationTargetPreference(this.label);

  final String label;

  TranslationLanguage? get fixedLanguage => switch (this) {
    followInterface => null,
    simplifiedChinese => TranslationLanguage.simplifiedChinese,
    english => TranslationLanguage.english,
    japanese => TranslationLanguage.japanese,
    korean => TranslationLanguage.korean,
  };
}

enum TranslationDisplayMode {
  originalOnly('原文'),
  chineseOnly('译文'),
  bilingual('双语');

  const TranslationDisplayMode(this.label);

  final String label;
}

enum TranslationDisplayTarget {
  title('标题'),
  category('分类'),
  tag('标签');

  const TranslationDisplayTarget(this.label);

  final String label;
}

enum AutomaticTranslationTarget {
  title('标题'),
  category('分类'),
  tag('标签');

  const AutomaticTranslationTarget(this.label);

  final String label;
}

@immutable
final class LocalizedTranslation {
  const LocalizedTranslation({
    required this.original,
    required this.translation,
    required this.mode,
  });

  final String original;
  final String? translation;
  final TranslationDisplayMode mode;

  bool get hasTranslation {
    final value = translation?.trim();
    return value != null && value.isNotEmpty && value != original.trim();
  }

  /// 表示翻译结果存在，即使它与原文完全相同。
  bool get hasResult {
    final value = translation?.trim();
    return value != null && value.isNotEmpty;
  }

  String get plainText {
    final translated = translation?.trim();
    if (mode == TranslationDisplayMode.originalOnly ||
        translated == null ||
        translated.isEmpty) {
      return original;
    }
    if (mode == TranslationDisplayMode.chineseOnly) return translated;
    return '$original | $translated';
  }
}

@immutable
final class TranslationEntry {
  const TranslationEntry({required this.english, required this.chinese});

  final String english;
  final String chinese;
}

enum TranslationAliasSource { userOverride, builtIn, learned }

enum TranslationCatalogSource {
  userOverride('用户'),
  learned('API'),
  builtIn('内置');

  const TranslationCatalogSource(this.label);

  final String label;
}

enum TranslationCatalogKind {
  title('标题'),
  category('分类'),
  tag('标签');

  const TranslationCatalogKind(this.label);

  final String label;
}

enum TranslationCatalogSort {
  updatedDesc('按最近更新排序'),
  originalAsc('按原文排序'),
  translationAsc('按译文排序'),
  source('按来源排序');

  const TranslationCatalogSort(this.label);

  final String label;
}

@immutable
final class TranslationCatalogItem {
  const TranslationCatalogItem({
    this.siteId = 'rule34video',
    this.sourceLanguageCode = 'und',
    this.targetLanguage = TranslationLanguage.simplifiedChinese,
    required this.kind,
    required this.canonicalName,
    required this.sourceText,
    required this.videoSlug,
    required this.builtInTranslation,
    required this.learnedTranslation,
    required this.userTranslation,
    required this.learnedProviderName,
    required this.learnedCreatedAt,
    required this.learnedUpdatedAt,
    required this.userUpdatedAt,
    required this.protectLearnedFromBuiltIn,
  });

  final String siteId;
  final String sourceLanguageCode;
  final TranslationLanguage targetLanguage;
  final TranslationCatalogKind kind;
  final String canonicalName;
  final String sourceText;
  final String? videoSlug;
  final String? builtInTranslation;
  final String? learnedTranslation;
  final String? userTranslation;
  final String? learnedProviderName;
  final DateTime? learnedCreatedAt;
  final DateTime? learnedUpdatedAt;
  final DateTime? userUpdatedAt;
  final bool protectLearnedFromBuiltIn;

  bool get hasBuiltIn => builtInTranslation?.isNotEmpty ?? false;
  bool get hasLearned => learnedTranslation?.isNotEmpty ?? false;
  bool get hasUserOverride => userTranslation?.isNotEmpty ?? false;

  String get effectiveTranslation =>
      userTranslation ??
      (protectLearnedFromBuiltIn ? learnedTranslation : null) ??
      builtInTranslation ??
      learnedTranslation ??
      '';

  TranslationCatalogSource get effectiveSource {
    if (hasUserOverride) return TranslationCatalogSource.userOverride;
    if (protectLearnedFromBuiltIn && hasLearned) {
      return TranslationCatalogSource.learned;
    }
    if (hasBuiltIn) return TranslationCatalogSource.builtIn;
    return TranslationCatalogSource.learned;
  }

  Set<TranslationCatalogSource> get sources => {
    if (hasUserOverride) TranslationCatalogSource.userOverride,
    if (hasLearned) TranslationCatalogSource.learned,
    if (hasBuiltIn) TranslationCatalogSource.builtIn,
  };

  DateTime? get updatedAt {
    final dates = [
      userUpdatedAt,
      learnedUpdatedAt,
    ].whereType<DateTime>().toList();
    if (dates.isEmpty) return null;
    dates.sort((left, right) => right.compareTo(left));
    return dates.first;
  }
}

enum TranslationMatchKind { exact, prefix, contains }

@immutable
final class TranslatedTagSuggestion {
  const TranslatedTagSuggestion({
    required this.english,
    required this.displayChinese,
    required this.matchedAlias,
    required this.aliasSource,
    required this.matchKind,
  });

  final String english;
  final String displayChinese;
  final String matchedAlias;
  final TranslationAliasSource aliasSource;
  final TranslationMatchKind matchKind;

  bool get matchedAlternateAlias => matchedAlias != displayChinese;
}

@immutable
final class TranslatedTitleSuggestion {
  const TranslatedTitleSuggestion({
    required this.videoId,
    required this.slug,
    this.siteId = 'rule34video',
    required this.english,
    required this.displayChinese,
    required this.aliasSource,
    required this.matchKind,
  });

  final String videoId;
  final String slug;
  final String siteId;
  final String english;
  final String displayChinese;
  final TranslationAliasSource aliasSource;
  final TranslationMatchKind matchKind;
}
