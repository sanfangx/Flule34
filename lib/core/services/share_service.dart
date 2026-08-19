import 'package:share_plus/share_plus.dart';

import '../models/video_models.dart';

abstract interface class ShareService {
  Future<void> shareVideo(VideoItem video);
}

final class PlatformShareService implements ShareService {
  @override
  Future<void> shareVideo(VideoItem video) async {
    final url = video.canonicalUri;
    await SharePlus.instance.share(
      ShareParams(
        title: video.title,
        subject: video.title,
        text: '${video.title}\n$url',
      ),
    );
  }
}
