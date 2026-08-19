/// Hanime1 专属搜索筛选模型。
///
/// hanime1.me 的筛选维度与 rule34video 完全不同（genre/sort/date/duration/
/// tags[]/brands[]/broad），因此独立建模，不与 [SearchFilters] 混用。
/// 选项值均为发送给网站的原始 searchKey（见 hanime1_search_options.g.dart）。
library;

/// Hanime1 发布日期筛选：近似时间预设，或指定年月（发送值形如“2026 年 8 月”）。
class HanimeDateFilter {
  const HanimeDateFilter.preset(String this.presetSearchKey)
    : year = null,
      month = null;

  const HanimeDateFilter.month({required this.year, required this.month})
    : presetSearchKey = null;

  /// 近似时间 searchKey（如“過去 24 小時”）；为 null 时表示指定年月。
  final String? presetSearchKey;

  /// 指定月份筛选的年（1~9999）；仅在非预设时非空。
  final int? year;

  /// 指定月份筛选的月（1~12）；仅在非预设时非空。
  final int? month;

  /// 发送给网站的 `date` 参数值。
  String? get searchKey {
    final preset = presetSearchKey;
    if (preset != null) return preset;
    final year = this.year;
    final month = this.month;
    if (year == null || month == null) return null;
    return '$year 年 $month 月';
  }

  /// 与另一个日期筛选是否等价（用于筛选 chips 的去重/清除判断）。
  @override
  bool operator ==(Object other) {
    return other is HanimeDateFilter &&
        other.presetSearchKey == presetSearchKey &&
        other.year == year &&
        other.month == month;
  }

  @override
  int get hashCode => Object.hash(presetSearchKey, year, month);

  @override
  String toString() => 'HanimeDateFilter(${searchKey ?? '未设置'})';
}

/// Hanime1 搜索筛选条件集合。
class HanimeSearchFilters {
  const HanimeSearchFilters({
    this.genre,
    this.sort,
    this.date,
    this.duration,
    this.tags = const {},
    this.brands = const {},
    this.broad = false,
  });

  static const Object _unset = Object();

  /// 分类（genre searchKey，如“裏番”）；null = 全部。
  final String? genre;

  /// 排序（sort searchKey，如“最新上市”）；null = 默认排序。
  final String? sort;

  /// 发布日期筛选；null = 全部。
  final HanimeDateFilter? date;

  /// 时长筛选（duration searchKey，如“10 分鐘 +”）；null = 全部。
  final String? duration;

  /// 标签 searchKey 集合（对应网站 `tags[]` 参数，多选）。
  final Set<String> tags;

  /// 品牌 searchKey 集合（对应网站 `brands[]` 参数，多选）。
  final Set<String> brands;

  /// 宽泛搜索开关（对应网站 `broad` 参数）。
  final bool broad;

  bool get isEmpty =>
      genre == null &&
      sort == null &&
      date == null &&
      duration == null &&
      tags.isEmpty &&
      brands.isEmpty &&
      !broad;

  int get activeCount {
    var count = 0;
    if (genre != null) count += 1;
    if (sort != null) count += 1;
    if (date != null) count += 1;
    if (duration != null) count += 1;
    if (broad) count += 1;
    count += tags.length + brands.length;
    return count;
  }

  HanimeSearchFilters copyWith({
    Object? genre = _unset,
    Object? sort = _unset,
    Object? date = _unset,
    Object? duration = _unset,
    Object? tags = _unset,
    Object? brands = _unset,
    bool? broad,
  }) {
    return HanimeSearchFilters(
      genre: identical(genre, _unset) ? this.genre : genre as String?,
      sort: identical(sort, _unset) ? this.sort : sort as String?,
      date: identical(date, _unset) ? this.date : date as HanimeDateFilter?,
      duration: identical(duration, _unset)
          ? this.duration
          : duration as String?,
      tags: identical(tags, _unset) ? this.tags : (tags as Set<String>).toSet(),
      brands: identical(brands, _unset)
          ? this.brands
          : (brands as Set<String>).toSet(),
      broad: broad ?? this.broad,
    );
  }

  @override
  String toString() {
    return 'HanimeSearchFilters(genre=$genre, sort=$sort, date=$date, '
        'duration=$duration, tags=$tags, brands=$brands, broad=$broad)';
  }
}

/// 从详情页等入口跳转 hanime 搜索页时的启动参数（经 go_router extra 传递）。
class HanimeSearchLaunch {
  const HanimeSearchLaunch({
    this.query = '',
    this.filters = const HanimeSearchFilters(),
  });

  final String query;
  final HanimeSearchFilters filters;

  bool get hasContent => query.trim().isNotEmpty || !filters.isEmpty;
}

/// 筛选条件摘要（用于日志与 UI 展示，不包含长列表的完整内容）。
String hanimeFiltersSummary(HanimeSearchFilters filters) {
  final parts = <String>[];
  if (filters.genre != null) parts.add('genre=${filters.genre}');
  if (filters.sort != null) parts.add('sort=${filters.sort}');
  if (filters.date != null) parts.add('date=${filters.date!.searchKey}');
  if (filters.duration != null) parts.add('duration=${filters.duration}');
  if (filters.tags.isNotEmpty) parts.add('tags=${filters.tags.length}个');
  if (filters.brands.isNotEmpty) parts.add('brands=${filters.brands.length}个');
  if (filters.broad) parts.add('broad');
  return parts.isEmpty ? '无' : parts.join('、');
}
