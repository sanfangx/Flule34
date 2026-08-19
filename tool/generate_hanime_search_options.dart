import 'dart:convert';
import 'dart:io';

/// 从 Han1meViewer (https://github.com/daisukiKaffuChino/Han1meViewer)
/// 的 assets/search_options/*.json 搬运 hanime1.me 搜索筛选选项，
/// 生成 lib/core/api/hanime1_search_options.g.dart。
///
/// 数据本身遵循 Apache-2.0 许可（见 THIRD_PARTY_NOTICES.md），
/// 此处仅作数据搬运：search_key 与多语言显示名均原样保留
/// （唯 sort_option.json 的 zh-rCN 两处繁体错字已顺手修正）。
Future<void> main(List<String> arguments) async {
  const dataDirectory = 'tool/data/hanime_search_options';
  const outputPath = 'lib/core/api/hanime1_search_options.g.dart';

  final genres = await _loadOptions('$dataDirectory/genre.json');
  final sorts = await _loadOptions('$dataDirectory/sort_option.json');
  final durations = await _loadOptions('$dataDirectory/duration.json');
  final releaseDates = await _loadOptions('$dataDirectory/release_date.json');
  final brands = await _loadBrands('$dataDirectory/brands.json');
  final tagGroups = await _loadTagGroups('$dataDirectory/tags.json');

  final buffer = StringBuffer()
    ..writeln('// GENERATED CODE - DO NOT MODIFY BY HAND.')
    ..writeln('// dart format off')
    ..writeln('//')
    ..writeln(
      '// 数据来源：Han1meViewer (https://github.com/daisukiKaffuChino/Han1meViewer)',
    )
    ..writeln(
      '// assets/search_options/*.json，Apache-2.0 许可，见 THIRD_PARTY_NOTICES.md。',
    )
    ..writeln('// 运行 tool/generate_hanime_search_options.dart 重新生成。')
    ..writeln()
    ..writeln('/// Hanime1 搜索筛选选项（数据搬运自 Han1meViewer）。')
    ..writeln('final class HanimeSearchOption {')
    ..writeln('  const HanimeSearchOption({')
    ..writeln('    required this.searchKey,')
    ..writeln('    required this.zh,')
    ..writeln('    required this.en,')
    ..writeln('    required this.ja,')
    ..writeln('    required this.tw,')
    ..writeln('  });')
    ..writeln()
    ..writeln('  /// 发送给 hanime1.me 的原始参数值；为 null 时表示“全部/不传该参数”。')
    ..writeln('  final String? searchKey;')
    ..writeln('  final String zh;')
    ..writeln('  final String en;')
    ..writeln('  final String ja;')
    ..writeln('  final String tw;')
    ..writeln()
    ..writeln('  String displayName(String localeCode) =>')
    ..writeln('      hanimeSearchOptionDisplayName(this, localeCode);')
    ..writeln('}')
    ..writeln()
    ..writeln('/// Hanime1 搜索标签分组（数据搬运自 Han1meViewer）。')
    ..writeln('final class HanimeTagGroup {')
    ..writeln('  const HanimeTagGroup({')
    ..writeln('    required this.id,')
    ..writeln('    required this.zh,')
    ..writeln('    required this.en,')
    ..writeln('    required this.ja,')
    ..writeln('    required this.tw,')
    ..writeln('    required this.options,')
    ..writeln('  });')
    ..writeln()
    ..writeln('  final String id;')
    ..writeln('  final String zh;')
    ..writeln('  final String en;')
    ..writeln('  final String ja;')
    ..writeln('  final String tw;')
    ..writeln('  final List<HanimeSearchOption> options;')
    ..writeln()
    ..writeln('  String displayName(String localeCode) =>')
    ..writeln('      hanimeTagGroupDisplayName(this, localeCode);')
    ..writeln('}')
    ..writeln()
    ..writeln('const hanimeGenres = <HanimeSearchOption>[${_options(genres)}];')
    ..writeln()
    ..writeln('const hanimeSorts = <HanimeSearchOption>[${_options(sorts)}];')
    ..writeln()
    ..writeln(
      'const hanimeDurations = <HanimeSearchOption>[${_options(durations)}];',
    )
    ..writeln()
    ..writeln(
      'const hanimeReleaseDates = <HanimeSearchOption>[${_options(releaseDates)}];',
    )
    ..writeln()
    ..writeln('const hanimeBrands = <HanimeSearchOption>[${_options(brands)}];')
    ..writeln()
    ..writeln(
      'const hanimeTagGroups = <HanimeTagGroup>[${_tagGroups(tagGroups)}];',
    )
    ..writeln()
    ..writeln(
      '/// 按应用语言码返回筛选选项显示名：zh*/zh_Hans*→简体，zh_Hant*/zh-TW→繁体，'
      'en*→英文，ja*→日文，其余兜底简体。',
    )
    ..writeln('String hanimeSearchOptionDisplayName(')
    ..writeln('  HanimeSearchOption option,')
    ..writeln('  String localeCode,')
    ..writeln(') {')
    ..writeln('  return _hanimeLocaleDisplayName(')
    ..writeln('    localeCode: localeCode,')
    ..writeln('    zh: option.zh,')
    ..writeln('    en: option.en,')
    ..writeln('    ja: option.ja,')
    ..writeln('    tw: option.tw,')
    ..writeln('  );')
    ..writeln('}')
    ..writeln()
    ..writeln('/// 按应用语言码返回标签分组显示名，规则同 hanimeSearchOptionDisplayName。')
    ..writeln(
      'String hanimeTagGroupDisplayName(HanimeTagGroup group, String localeCode) {',
    )
    ..writeln('  return _hanimeLocaleDisplayName(')
    ..writeln('    localeCode: localeCode,')
    ..writeln('    zh: group.zh,')
    ..writeln('    en: group.en,')
    ..writeln('    ja: group.ja,')
    ..writeln('    tw: group.tw,')
    ..writeln('  );')
    ..writeln('}')
    ..writeln()
    ..writeln('String _hanimeLocaleDisplayName({')
    ..writeln('  required String localeCode,')
    ..writeln('  required String zh,')
    ..writeln('  required String en,')
    ..writeln('  required String ja,')
    ..writeln('  required String tw,')
    ..writeln('}) {')
    ..writeln('  final lower = localeCode.toLowerCase();')
    ..writeln('  if (lower.startsWith(\'zh\') &&')
    ..writeln('      (lower.contains(\'hant\') || lower.contains(\'-tw\') ||')
    ..writeln('          lower.contains(\'_tw\'))) {')
    ..writeln('    return tw;')
    ..writeln('  }')
    ..writeln('  if (lower.startsWith(\'zh\')) return zh;')
    ..writeln('  if (lower.startsWith(\'en\')) return en;')
    ..writeln('  if (lower.startsWith(\'ja\')) return ja;')
    ..writeln('  return zh;')
    ..writeln('}')
    ..writeln('// dart format on');

  final output = File(outputPath);
  await output.parent.create(recursive: true);
  await output.writeAsString(buffer.toString());

  stdout.writeln(
    '已生成：genre=${genres.length}、sort=${sorts.length}、'
    'duration=${durations.length}、releaseDate=${releaseDates.length}、'
    'brand=${brands.length}、tagGroup=${tagGroups.length}'
    '（标签共 ${tagGroups.fold<int>(0, (sum, group) => sum + group.options.length)} 个）',
  );
}

/// 统一选项：lang（四语）+ search_key（可 null）。
Future<List<_OptionData>> _loadOptions(String path) async {
  final raw = jsonDecode(await File(path).readAsString());
  if (raw is! List) throw FormatException('选项文件格式无效：$path');
  return raw.map((item) => _optionFromJson(item, path)).toList();
}

/// 品牌选项：只有 name（作为全部语言显示名）+ search_key。
Future<List<_OptionData>> _loadBrands(String path) async {
  final raw = jsonDecode(await File(path).readAsString());
  if (raw is! List) throw FormatException('品牌文件格式无效：$path');
  return raw.map((item) {
    final map = (item as Map).cast<String, Object?>();
    final name = map['name'] as String;
    return _OptionData(
      searchKey: map['search_key'] as String?,
      zh: name,
      en: name,
      ja: name,
      tw: name,
    );
  }).toList();
}

/// 标签：Map<分组 id, List<选项>>，选项含 name + lang + search_key。
Future<List<_TagGroupData>> _loadTagGroups(String path) async {
  final raw = jsonDecode(await File(path).readAsString());
  if (raw is! Map) throw FormatException('标签文件格式无效：$path');
  final result = <_TagGroupData>[];
  for (final entry in raw.entries) {
    final id = entry.key as String;
    final names = _tagGroupNames[id];
    if (names == null) throw StateError('缺少分组名称映射：$id');
    final list = entry.value as List;
    final options = list.map((item) => _optionFromJson(item, path)).toList();
    result.add(
      _TagGroupData(
        id: id,
        zh: names.$1,
        en: names.$2,
        ja: names.$3,
        tw: names.$4,
        options: options,
      ),
    );
  }
  return result;
}

// 分组显示名：zh、en、ja、tw（组名 zh-rCN/zh-rTW 来自 Han1meViewer strings.xml，
// ja 由本项目补充）。
const _tagGroupNames = <String, (String, String, String, String)>{
  'video_attributes': ('影片属性', 'Video Attributes', 'ビデオ属性', '影片屬性'),
  'character_relationships': (
    '人物关系',
    'Character Relationships',
    'キャラクター関係',
    '人物關係',
  ),
  'characteristics': ('角色设定', 'Characteristics', '特性', '角色設定'),
  'appearance_and_figure': ('外貌身材', 'Appearance and Figure', '外見と体格', '外貌身材'),
  'story_location': ('情景场所', 'Scenario and Environment', 'シチュエーション', '情境場所'),
  'story_plot': ('故事剧情', 'Story Plot', 'ストーリー', '故事劇情'),
  'sex_positions': ('性交体位', 'Sex Positions', '性交体位', '性交體位'),
};

_OptionData _optionFromJson(Object item, String path) {
  final map = (item as Map).cast<String, Object?>();
  final lang = (map['lang'] as Map?)?.cast<String, Object?>() ?? const {};
  final searchKey = map['search_key'] as String?;
  final zhRaw = lang['zh-rCN'];
  final hasDisplayName =
      map['name'] is String || (zhRaw is String && zhRaw.trim().isNotEmpty);
  if (searchKey == null && !hasDisplayName) {
    throw FormatException('选项缺少 search_key 或显示名：$path $item');
  }
  return _OptionData(
    searchKey: searchKey,
    zh: (lang['zh-rCN'] ?? map['name'] ?? '').toString(),
    en: (lang['en'] ?? map['name'] ?? '').toString(),
    ja: (lang['ja'] ?? map['name'] ?? '').toString(),
    tw: (lang['zh-rTW'] ?? map['name'] ?? '').toString(),
  );
}

String _options(List<_OptionData> options) {
  return options
      .map(
        (option) =>
            '\n    HanimeSearchOption('
            'searchKey: ${option.searchKey == null ? 'null' : jsonEncode(option.searchKey)}, '
            'zh: ${jsonEncode(option.zh)}, en: ${jsonEncode(option.en)}, '
            'ja: ${jsonEncode(option.ja)}, tw: ${jsonEncode(option.tw)}),',
      )
      .join()
      .trim();
}

String _tagGroups(List<_TagGroupData> groups) {
  return groups
      .map(
        (group) =>
            '\n    HanimeTagGroup('
            'id: ${jsonEncode(group.id)}, zh: ${jsonEncode(group.zh)}, '
            'en: ${jsonEncode(group.en)}, ja: ${jsonEncode(group.ja)}, '
            'tw: ${jsonEncode(group.tw)}, '
            'options: <HanimeSearchOption>[${_options(group.options)}]),',
      )
      .join()
      .trim();
}

final class _OptionData {
  const _OptionData({
    required this.searchKey,
    required this.zh,
    required this.en,
    required this.ja,
    required this.tw,
  });

  final String? searchKey;
  final String zh;
  final String en;
  final String ja;
  final String tw;
}

final class _TagGroupData {
  const _TagGroupData({
    required this.id,
    required this.zh,
    required this.en,
    required this.ja,
    required this.tw,
    required this.options,
  });

  final String id;
  final String zh;
  final String en;
  final String ja;
  final String tw;
  final List<_OptionData> options;
}
