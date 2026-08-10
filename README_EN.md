# Flule34

[简体中文](README.md) | **English** | [日本語](README_JA.md) | [한국어](README_KO.md)

Flule34 is an unofficial Flutter client for Rule34Video on Android. It uses the website's existing pages, endpoints, and video sources while improving mobile browsing, filtering, playback, downloads, and local organization.

This project is not affiliated with Rule34Video. It is intended only for users who have reached the legal age of adulthood in their jurisdiction and are legally allowed to access this content.

## Features

### Browse and filter

- Latest, popular, top-rated, and followed feeds;
- Single-column and masonry-style two-column layouts;
- Search for videos, tags, categories, artists, and uploaders;
- Combine tags, artists, categories, content preference, duration, upload period, rating, vote count, exclusions, and intersection rules;
- Video cards show upload time, views, rating, votes, and duration.

### Playback

- Prefers 1080p and falls back to the best lower quality; supports 2160p sources when available;
- Persistent video cache, playback position, speed, and quality preferences;
- Full-screen controls, orientation preferences, background playback, keep-awake, and looping;
- Hold the video for 500 ms to play temporarily at 2x speed with a subtle indicator;
- A centered loading spinner distinguishes rebuffering from pause.

### Library

- Website favorites, watch history, and artist/uploader subscriptions;
- Account-independent local libraries with custom collections;
- Curated built-in creator libraries that preserve user changes during upgrades;
- Search and filters across favorites, history, and local libraries;
- Account playlists with create, rename, membership management, continuous playback, looping modes, and next-item prefetch.

### Downloads and account

- Downloads to the public `Download/Flule34` directory;
- Background tasks, notifications, pause/resume, retries, and task restoration;
- Validation for externally deleted, renamed, or changed files;
- Login cookies and optional credentials stored with Android secure storage;
- Session recovery without blocking public playback.

### Languages and content translation

- The interface can follow the system or use Simplified Chinese, English, Japanese, or Korean;
- Content translation can follow the interface or independently target any of those four languages;
- A built-in Simplified Chinese tag/category dictionary is included. Other target languages use configured providers or manual translations;
- The translation library manages built-in, API-generated, and user translations with language/type/source filters, search, sorting, editing, and batch operations;
- Versioned JSON import/export preserves target-language metadata. Imports merge API and user layers and never replace the built-in dictionary;
- Multiple Chat Completions, Responses, Anthropic Messages, DeepL, or MyMemory providers can be reordered and used as fallbacks;
- AI reasoning parameters are probed once per service, then the successful strategy is persisted;
- Automatic translation is opt-in separately for titles, categories, and tags. Results are stored as durable local data;
- Mixed-language source text is not skipped by local detection: AI and DeepL detect it, while MyMemory uses conservative script inference only because its API requires a source language pair;
- Search combines the website query with reverse lookup through locally stored title and tag translations.

## Install

Download the latest `arm64-v8a` APK from [GitHub Releases](https://github.com/Hanestl/Flule34/releases/latest).

Flule34 supports Android 7.0 (API 24) and later on ARM64 phones and tablets. Android may ask you to allow installation from your browser or file manager. Use `SHA256SUMS.txt` from the release to verify the APK.

## Data and privacy

- Local libraries and download records stay on the device and are independent of the website account;
- Favorites, history, subscriptions, and playlists belong to the signed-in website account;
- Downloaded files remain in the public directory after uninstalling the app;
- No advertising, analytics, or third-party crash-reporting SDK is included;
- Redacted diagnostic logs are kept locally for seven days and can be exported or cleared under Privacy & Data. They are never uploaded automatically;
- See [PRIVACY.md](PRIVACY.md) for details.

## Build

Verified toolchain: Flutter 3.44.8, Dart 3.12.2, JDK 17, and Android SDK 36.

```powershell
flutter pub get
dart run build_runner build
flutter analyze --no-pub
flutter test --no-pub
flutter build apk --release --split-per-abi --target-platform android-arm64 --no-pub
```

The APK is written to `build/app/outputs/flutter-apk/app-arm64-v8a-release.apk`. Database changes also require updated Drift schema snapshots and migration tests.

## Known limitations

- Browsing, details, and account features depend on the website's HTML structure;
- Expiring video URLs may need to be fetched again;
- The project does not bypass permissions, paywalls, or regional restrictions.

## License

Flule34 is licensed under the [MIT License](LICENSE). Third-party license notices are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
