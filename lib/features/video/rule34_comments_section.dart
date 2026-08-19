import 'package:flutter/material.dart';
import 'package:flule34/l10n/ui_localization.dart';

import '../../core/api/rule34video_api.dart';
import '../../core/models/content_source.dart';
import '../../core/models/rule34_comment_models.dart';
import '../../core/models/video_models.dart';
import '../../shared/site_avatar.dart';
import '../auth/login_sheet.dart';

class Rule34CommentsSection extends StatefulWidget {
  const Rule34CommentsSection({
    super.key,
    required this.api,
    required this.video,
  });

  final Rule34VideoApi api;
  final VideoItem video;

  @override
  State<Rule34CommentsSection> createState() => _Rule34CommentsSectionState();
}

class _Rule34CommentsSectionState extends State<Rule34CommentsSection> {
  final _commentController = TextEditingController();
  final _composerFocus = FocusNode();
  Future<List<Rule34VideoComment>>? _future;
  var _submitting = false;

  @override
  void initState() {
    super.initState();
    _future = _load();
    _composerFocus.addListener(_onFocusChanged);
  }

  @override
  void dispose() {
    _composerFocus.removeListener(_onFocusChanged);
    _composerFocus.dispose();
    _commentController.dispose();
    super.dispose();
  }

  void _onFocusChanged() {
    if (mounted) setState(() {});
  }

  Future<List<Rule34VideoComment>> _load() =>
      widget.api.loadComments(widget.video);

  Future<void> _refresh() async {
    final future = _load();
    setState(() => _future = future);
    await future;
  }

  Future<void> _submitComment() async {
    final text = _commentController.text.trim();
    if (text.isEmpty || _submitting) return;
    setState(() => _submitting = true);
    try {
      await widget.api.postComment(video: widget.video, text: text);
      _commentController.clear();
      _composerFocus.unfocus();
      if (mounted) {
        ScaffoldMessenger.of(
          context,
        ).showSnackBar(const SnackBar(content: AppText('评论已提交，审核通过后展示。')));
      }
      await _refresh();
    } catch (error) {
      if (mounted) {
        ScaffoldMessenger.of(
          context,
        ).showSnackBar(SnackBar(content: AppText('发表失败：$error')));
      }
    } finally {
      if (mounted) setState(() => _submitting = false);
    }
  }

  Future<void> _ensureLogin() async {
    if (!widget.api.sessionStore.isLoggedIn) {
      await showLoginSheet(context, widget.api);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(12, 8, 12, 8),
      child: Column(
        children: [
          Expanded(child: _buildList()),
          const SizedBox(height: 6),
          if (widget.api.sessionStore.isLoggedIn)
            _buildComposer()
          else
            OutlinedButton.icon(
              onPressed: _ensureLogin,
              icon: const Icon(Icons.login),
              label: const AppText('登录 R34V 后参与评论'),
            ),
        ],
      ),
    );
  }

  Widget _buildList() {
    return FutureBuilder<List<Rule34VideoComment>>(
      future: _future,
      builder: (context, snapshot) {
        if (snapshot.connectionState != ConnectionState.done) {
          return const Center(child: CircularProgressIndicator());
        }
        if (snapshot.hasError) {
          return Center(
            child: OutlinedButton.icon(
              onPressed: _refresh,
              icon: const Icon(Icons.refresh),
              label: const AppText('评论加载失败，点击重试'),
            ),
          );
        }
        final comments = snapshot.data ?? const <Rule34VideoComment>[];
        if (comments.isEmpty) return const Center(child: AppText('还没有评论。'));
        return RefreshIndicator(
          onRefresh: _refresh,
          child: ListView.builder(
            itemCount: comments.length,
            itemBuilder: (context, index) => _buildComment(comments[index]),
          ),
        );
      },
    );
  }

  Widget _buildComposer() {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.end,
      children: [
        Expanded(
          child: TextField(
            controller: _commentController,
            focusNode: _composerFocus,
            minLines: 1,
            maxLines: _composerFocus.hasFocus ? 4 : 1,
            textInputAction: TextInputAction.newline,
            decoration: InputDecoration(
              hintText: context.uiText('发一条评论...'),
              border: const OutlineInputBorder(),
              isDense: true,
            ),
          ),
        ),
        const SizedBox(width: 6),
        IconButton.filled(
          tooltip: '发送',
          onPressed: _submitting ? null : _submitComment,
          icon: _submitting
              ? const SizedBox.square(
                  dimension: 18,
                  child: CircularProgressIndicator(strokeWidth: 2),
                )
              : const Icon(Icons.send),
        ),
      ],
    );
  }

  Widget _buildComment(Rule34VideoComment comment) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SiteAvatar(
            radius: 16,
            imageUrl: comment.avatarUrl,
            fallbackIcon: Icons.person,
            site: ContentSite.rule34video,
          ),
          const SizedBox(width: 8),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Expanded(
                      child: Text(
                        comment.username,
                        style: Theme.of(context).textTheme.labelMedium,
                      ),
                    ),
                    if (comment.dateLabel != null)
                      AppText(
                        comment.dateLabel!,
                        style: Theme.of(context).textTheme.bodySmall,
                      ),
                  ],
                ),
                const SizedBox(height: 2),
                AppText(comment.content),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
