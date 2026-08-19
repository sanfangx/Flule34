enum ContentSite {
  rule34video(
    id: 'rule34video',
    label: 'Rule34Video',
    baseUrl: 'https://rule34video.com',
    capabilities: ContentSiteCapabilities(
      accountFavorites: true,
      accountPlaylists: true,
      subscriptions: true,
      metadataCollections: true,
      uploaderProfiles: true,
      advancedFilters: true,
      videoPreviews: true,
    ),
  ),
  hanime1(
    id: 'hanime1',
    label: 'Hanime',
    baseUrl: 'https://hanime1.me',
    capabilities: ContentSiteCapabilities(videoPreviews: true),
  );

  const ContentSite({
    required this.id,
    required this.label,
    required this.baseUrl,
    required this.capabilities,
  });

  final String id;
  final String label;
  final String baseUrl;
  final ContentSiteCapabilities capabilities;

  Uri get origin => Uri.parse('$baseUrl/');

  static ContentSite fromId(String? value) {
    for (final site in values) {
      if (site.id == value) return site;
    }
    return ContentSite.rule34video;
  }
}

final class ContentSiteCapabilities {
  const ContentSiteCapabilities({
    this.accountFavorites = false,
    this.accountPlaylists = false,
    this.subscriptions = false,
    this.metadataCollections = false,
    this.uploaderProfiles = false,
    this.advancedFilters = false,
    this.videoPreviews = false,
  });

  final bool accountFavorites;
  final bool accountPlaylists;
  final bool subscriptions;
  final bool metadataCollections;
  final bool uploaderProfiles;
  final bool advancedFilters;
  final bool videoPreviews;
}

extension ContentSiteHeaders on ContentSite {
  Map<String, String> mediaHeaders({String? cookie}) {
    final headers = <String, String>{
      'User-Agent':
          'Mozilla/5.0 (Linux; Android 13; Mobile) AppleWebKit/537.36 '
          '(KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
      'Referer': '$baseUrl/',
      'Accept': '*/*',
    };
    if (cookie != null && cookie.trim().isNotEmpty) {
      headers['Cookie'] = cookie.trim();
    }
    return headers;
  }
}
