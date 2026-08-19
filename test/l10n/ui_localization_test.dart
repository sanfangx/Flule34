import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:flule34/l10n/ui_localization.dart';

void main() {
  test('四种界面语言使用各自文案', () {
    expect(localizeUiText(const Locale('zh'), '媒体库'), '媒体库');
    expect(localizeUiText(const Locale('en'), '媒体库'), 'Library');
    expect(localizeUiText(const Locale('ja'), '媒体库'), 'ライブラリ');
    expect(localizeUiText(const Locale('ko'), '媒体库'), '라이브러리');
  });

  test('不支持的系统语言回退到简体中文', () {
    expect(localizeUiText(const Locale('fr'), '翻译设置'), '翻译设置');
  });

  test('动态文案模板保留插值内容', () {
    expect(localizeUiText(const Locale('en'), '已选择 12 项'), contains('12'));
    expect(localizeUiText(const Locale('ja'), '已选择 12 项'), contains('12'));
    expect(localizeUiText(const Locale('ko'), '已选择 12 项'), contains('12'));
  });

  test('关键页面文案均有英日韩译文', () {
    const sources = [
      '内容取向',
      '时长',
      '发布时间',
      '排序',
      '必须同时包含',
      '尚未选择标签',
      '按标签和内容主题探索',
      '本地分类库',
      '视频保存路径：Download/Flule34',
      '当前开发构建未配置更新源',
      '此构建未配置 GitHub Releases 更新源。',
      '艺术家',
      '分类',
      '标签',
    ];
    for (final source in sources) {
      expect(localizeUiText(const Locale('en'), source), isNot(source));
      expect(localizeUiText(const Locale('ja'), source), isNot(source));
      expect(localizeUiText(const Locale('ko'), source), isNot(source));
    }
  });

  test('翻译库完整统计模板不会遗留中文片段', () {
    const source = '共 10101 条 · 内置 9990 · API 100 · 用户 11';
    expect(
      localizeUiText(const Locale('en'), source),
      'Total 10101 items · Built-in 9990 · API 100 · User 11',
    );
    expect(localizeUiText(const Locale('ja'), source), isNot(contains('共')));
    expect(localizeUiText(const Locale('ko'), source), isNot(contains('用户')));
  });
}
