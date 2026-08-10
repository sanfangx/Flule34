import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:intl/intl.dart' as intl;

import 'app_localizations_en.dart';
import 'app_localizations_ja.dart';
import 'app_localizations_ko.dart';
import 'app_localizations_zh.dart';

// ignore_for_file: type=lint

/// Callers can lookup localized strings with an instance of AppLocalizations
/// returned by `AppLocalizations.of(context)`.
///
/// Applications need to include `AppLocalizations.delegate()` in their app's
/// `localizationDelegates` list, and the locales they support in the app's
/// `supportedLocales` list. For example:
///
/// ```dart
/// import 'generated/app_localizations.dart';
///
/// return MaterialApp(
///   localizationsDelegates: AppLocalizations.localizationsDelegates,
///   supportedLocales: AppLocalizations.supportedLocales,
///   home: MyApplicationHome(),
/// );
/// ```
///
/// ## Update pubspec.yaml
///
/// Please make sure to update your pubspec.yaml to include the following
/// packages:
///
/// ```yaml
/// dependencies:
///   # Internationalization support.
///   flutter_localizations:
///     sdk: flutter
///   intl: any # Use the pinned version from flutter_localizations
///
///   # Rest of dependencies
/// ```
///
/// ## iOS Applications
///
/// iOS applications define key application metadata, including supported
/// locales, in an Info.plist file that is built into the application bundle.
/// To configure the locales supported by your app, you’ll need to edit this
/// file.
///
/// First, open your project’s ios/Runner.xcworkspace Xcode workspace file.
/// Then, in the Project Navigator, open the Info.plist file under the Runner
/// project’s Runner folder.
///
/// Next, select the Information Property List item, select Add Item from the
/// Editor menu, then select Localizations from the pop-up menu.
///
/// Select and expand the newly-created Localizations item then, for each
/// locale your application supports, add a new item and select the locale
/// you wish to add from the pop-up menu in the Value field. This list should
/// be consistent with the languages listed in the AppLocalizations.supportedLocales
/// property.
abstract class AppLocalizations {
  AppLocalizations(String locale)
    : localeName = intl.Intl.canonicalizedLocale(locale.toString());

  final String localeName;

  static AppLocalizations of(BuildContext context) {
    return Localizations.of<AppLocalizations>(context, AppLocalizations)!;
  }

  static const LocalizationsDelegate<AppLocalizations> delegate =
      _AppLocalizationsDelegate();

  /// A list of this localizations delegate along with the default localizations
  /// delegates.
  ///
  /// Returns a list of localizations delegates containing this delegate along with
  /// GlobalMaterialLocalizations.delegate, GlobalCupertinoLocalizations.delegate,
  /// and GlobalWidgetsLocalizations.delegate.
  ///
  /// Additional delegates can be added by appending to this list in
  /// MaterialApp. This list does not have to be used at all if a custom list
  /// of delegates is preferred or required.
  static const List<LocalizationsDelegate<dynamic>> localizationsDelegates =
      <LocalizationsDelegate<dynamic>>[
        delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ];

  /// A list of this localizations delegate's supported locales.
  static const List<Locale> supportedLocales = <Locale>[
    Locale('en'),
    Locale('ja'),
    Locale('ko'),
    Locale('zh'),
  ];

  /// Flule34 UI: 20–60 分钟
  ///
  /// In zh, this message translates to:
  /// **'20–60 分钟'**
  String get ui0aedf15f;

  /// Flule34 UI: 5 分钟以内
  ///
  /// In zh, this message translates to:
  /// **'5 分钟以内'**
  String get ui4ebe1e15;

  /// Flule34 UI: 5–20 分钟
  ///
  /// In zh, this message translates to:
  /// **'5–20 分钟'**
  String get ui594005ec;

  /// Flule34 UI: 60 分钟以上
  ///
  /// In zh, this message translates to:
  /// **'60 分钟以上'**
  String get ui0be8a2c8;

  /// Flule34 UI: ===== 最近 7 天日志 =====
  ///
  /// In zh, this message translates to:
  /// **'===== 最近 7 天日志 ====='**
  String get ui6e93de1b;

  /// Flule34 UI: ===== 诊断信息 =====
  ///
  /// In zh, this message translates to:
  /// **'===== 诊断信息 ====='**
  String get ui2e77e7e1;

  /// Flule34 UI: App 设置
  ///
  /// In zh, this message translates to:
  /// **'App 设置'**
  String get ui186386f2;

  /// Flule34 UI: DeepL 套餐与端点
  ///
  /// In zh, this message translates to:
  /// **'DeepL 套餐与端点'**
  String get ui14d5d228;

  /// Flule34 UI: Flule34 本地诊断日志
  ///
  /// In zh, this message translates to:
  /// **'Flule34 本地诊断日志'**
  String get ui5532d8d0;

  /// Flule34 UI: Flule34 翻译库
  ///
  /// In zh, this message translates to:
  /// **'Flule34 翻译库'**
  String get ui514d16fd;

  /// Flule34 UI: Git 提交
  ///
  /// In zh, this message translates to:
  /// **'Git 提交'**
  String get ui57e4db6c;

  /// Flule34 UI: GitHub 暂时拒绝了更新请求，请稍后重试或更换网络。
  ///
  /// In zh, this message translates to:
  /// **'GitHub 暂时拒绝了更新请求，请稍后重试或更换网络。'**
  String get ui4554eb7e;

  /// Flule34 UI: GitHub 源代码
  ///
  /// In zh, this message translates to:
  /// **'GitHub 源代码'**
  String get ui1bcd541a;

  /// Flule34 UI: MyMemory 可用邮箱标识提高免费额度。
  ///
  /// In zh, this message translates to:
  /// **'MyMemory 可用邮箱标识提高免费额度。'**
  String get ui103930a8;

  /// Flule34 UI: Rule34Video 账号
  ///
  /// In zh, this message translates to:
  /// **'Rule34Video 账号'**
  String get ui2c98e3c6;

  /// Flule34 UI: Wi-Fi 使用默认清晰度，移动网络最高 480p
  ///
  /// In zh, this message translates to:
  /// **'Wi-Fi 使用默认清晰度，移动网络最高 480p'**
  String get ui45943bf3;

  /// Flule34 UI: Wi-Fi 最高 720p，移动网络最高 360p
  ///
  /// In zh, this message translates to:
  /// **'Wi-Fi 最高 720p，移动网络最高 360p'**
  String get ui34eda443;

  /// Flule34 UI: {p0} · 已下载
  ///
  /// In zh, this message translates to:
  /// **'{p0} · 已下载'**
  String ui3bebb943(String p0);

  /// Flule34 UI: {p0} · 已失效
  ///
  /// In zh, this message translates to:
  /// **'{p0} · 已失效'**
  String ui152a8991(String p0);

  /// Flule34 UI: {p0} · 正在校验
  ///
  /// In zh, this message translates to:
  /// **'{p0} · 正在校验'**
  String ui409b192f(String p0);

  /// Flule34 UI: {p0} · 生效
  ///
  /// In zh, this message translates to:
  /// **'{p0} · 生效'**
  String ui1e263a03(String p0);

  /// Flule34 UI: {p0} 个视频
  ///
  /// In zh, this message translates to:
  /// **'{p0} 个视频'**
  String ui167ae392(String p0);

  /// Flule34 UI: {p0} 已加入下载队列。
  ///
  /// In zh, this message translates to:
  /// **'{p0} 已加入下载队列。'**
  String ui4e278fff(String p0);

  /// Flule34 UI: {p0} 已在下载管理中。
  ///
  /// In zh, this message translates to:
  /// **'{p0} 已在下载管理中。'**
  String ui5e77ec72(String p0);

  /// Flule34 UI: {p0} 次观看
  ///
  /// In zh, this message translates to:
  /// **'{p0} 次观看'**
  String ui67c16b0b(String p0);

  /// Flule34 UI: {p0} 正在加入下载队列。
  ///
  /// In zh, this message translates to:
  /// **'{p0} 正在加入下载队列。'**
  String ui3455223c(String p0);

  /// Flule34 UI: {p0} 票
  ///
  /// In zh, this message translates to:
  /// **'{p0} 票'**
  String ui7025b0dd(String p0);

  /// Flule34 UI: {p0} 连接成功
  ///
  /// In zh, this message translates to:
  /// **'{p0} 连接成功'**
  String ui69ba5039(String p0);

  /// Flule34 UI: {p0}% · {p1} 票
  ///
  /// In zh, this message translates to:
  /// **'{p0}% · {p1} 票'**
  String ui44f14c54(String p0, String p1);

  /// Flule34 UI: {p0}{p1}；译文：{p2}{p3}
  ///
  /// In zh, this message translates to:
  /// **'{p0}{p1}；译文：{p2}{p3}'**
  String ui278d8aed(String p0, String p1, String p2, String p3);

  /// Flule34 UI: {p0}（内置新增
  ///
  /// In zh, this message translates to:
  /// **'{p0}（内置新增'**
  String ui581b1dd5(String p0);

  /// Flule34 UI: {p0}（内置新增 v{p1}）
  ///
  /// In zh, this message translates to:
  /// **'{p0}（内置新增 v{p1}）'**
  String ui5ab8d170(String p0, String p1);

  /// Flule34 UI: {p0}（精选 {p1}）
  ///
  /// In zh, this message translates to:
  /// **'{p0}（精选 {p1}）'**
  String ui13d9e100(String p0, String p1);

  /// Flule34 UI: 一列
  ///
  /// In zh, this message translates to:
  /// **'一列'**
  String get ui2046553b;

  /// Flule34 UI: 上一个
  ///
  /// In zh, this message translates to:
  /// **'上一个'**
  String get ui0b8ef7e3;

  /// Flule34 UI: 上传者
  ///
  /// In zh, this message translates to:
  /// **'上传者'**
  String get ui5e2af7ea;

  /// Flule34 UI: 上传者资料加载失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'上传者资料加载失败：{p0}'**
  String ui772dc31b(String p0);

  /// Flule34 UI: 下一个
  ///
  /// In zh, this message translates to:
  /// **'下一个'**
  String get ui58a06980;

  /// Flule34 UI: 下载
  ///
  /// In zh, this message translates to:
  /// **'下载'**
  String get ui175900a0;

  /// Flule34 UI: 下载任务已被系统中断，请重试。
  ///
  /// In zh, this message translates to:
  /// **'下载任务已被系统中断，请重试。'**
  String get ui564d53e4;

  /// Flule34 UI: 下载任务被系统中断，请重试。
  ///
  /// In zh, this message translates to:
  /// **'下载任务被系统中断，请重试。'**
  String get ui5cfc38c2;

  /// Flule34 UI: 下载失败
  ///
  /// In zh, this message translates to:
  /// **'下载失败'**
  String get ui16f20943;

  /// Flule34 UI: 下载属于本机功能，退出登录不会取消下载或删除公共目录中的文件。
  ///
  /// In zh, this message translates to:
  /// **'下载属于本机功能，退出登录不会取消下载或删除公共目录中的文件。'**
  String get ui07298d42;

  /// Flule34 UI: 下载文件
  ///
  /// In zh, this message translates to:
  /// **'下载文件'**
  String get ui29e8ad9e;

  /// Flule34 UI: 下载文件和记录已删除。
  ///
  /// In zh, this message translates to:
  /// **'下载文件和记录已删除。'**
  String get ui5ecf7c24;

  /// Flule34 UI: 下载文件已失效或没有可播放此 MP4 的应用。
  ///
  /// In zh, this message translates to:
  /// **'下载文件已失效或没有可播放此 MP4 的应用。'**
  String get ui7fc5cfeb;

  /// Flule34 UI: 下载清晰度
  ///
  /// In zh, this message translates to:
  /// **'下载清晰度'**
  String get ui180a6fbf;

  /// Flule34 UI: 下载记录已删除。
  ///
  /// In zh, this message translates to:
  /// **'下载记录已删除。'**
  String get ui3187db03;

  /// Flule34 UI: 下载设置
  ///
  /// In zh, this message translates to:
  /// **'下载设置'**
  String get ui49483396;

  /// Flule34 UI: 不会删除下载的视频或账号数据。
  ///
  /// In zh, this message translates to:
  /// **'不会删除下载的视频或账号数据。'**
  String get ui350fa41c;

  /// Flule34 UI: 不存在
  ///
  /// In zh, this message translates to:
  /// **'不存在'**
  String get ui10ebf8e5;

  /// Flule34 UI: 不限
  ///
  /// In zh, this message translates to:
  /// **'不限'**
  String get ui34e49ede;

  /// Flule34 UI: 不限时长
  ///
  /// In zh, this message translates to:
  /// **'不限时长'**
  String get ui6c2ca0b8;

  /// Flule34 UI: 不限时间
  ///
  /// In zh, this message translates to:
  /// **'不限时间'**
  String get ui733128eb;

  /// Flule34 UI: 两列
  ///
  /// In zh, this message translates to:
  /// **'两列'**
  String get ui7447788f;

  /// Flule34 UI: 主题
  ///
  /// In zh, this message translates to:
  /// **'主题'**
  String get ui557a9537;

  /// Flule34 UI: 主题模式
  ///
  /// In zh, this message translates to:
  /// **'主题模式'**
  String get ui7b7ae9f2;

  /// Flule34 UI: 仅 Wi-Fi 下载
  ///
  /// In zh, this message translates to:
  /// **'仅 Wi-Fi 下载'**
  String get ui11b84182;

  /// Flule34 UI: 仅使用 Wi-Fi 下载
  ///
  /// In zh, this message translates to:
  /// **'仅使用 Wi-Fi 下载'**
  String get ui3d863311;

  /// Flule34 UI: 仅保存在本机，自动脱敏，保留最近 7 天。
  /// {p0}
  ///
  /// In zh, this message translates to:
  /// **'仅保存在本机，自动脱敏，保留最近 7 天。\n{p0}'**
  String ui49859040(String p0);

  /// Flule34 UI: 仅删除记录
  ///
  /// In zh, this message translates to:
  /// **'仅删除记录'**
  String get ui3bf7470b;

  /// Flule34 UI: 仅在视频正在播放时生效，暂停或离开页面后自动恢复。
  ///
  /// In zh, this message translates to:
  /// **'仅在视频正在播放时生效，暂停或离开页面后自动恢复。'**
  String get ui730f65d7;

  /// Flule34 UI: 仅显示已验证上传者
  ///
  /// In zh, this message translates to:
  /// **'仅显示已验证上传者'**
  String get ui709d26fa;

  /// Flule34 UI: 仅登录后按账号保存；关闭后不再记录新搜索。
  ///
  /// In zh, this message translates to:
  /// **'仅登录后按账号保存；关闭后不再记录新搜索。'**
  String get ui51418311;

  /// Flule34 UI: 从头连续播放
  ///
  /// In zh, this message translates to:
  /// **'从头连续播放'**
  String get ui44ac200e;

  /// Flule34 UI: 你可以只删除下载记录并保留视频，也可以同时删除公共目录中的视频。
  ///
  /// In zh, this message translates to:
  /// **'你可以只删除下载记录并保留视频，也可以同时删除公共目录中的视频。'**
  String get ui4a42f091;

  /// Flule34 UI: 使用翻译服务
  ///
  /// In zh, this message translates to:
  /// **'使用翻译服务'**
  String get ui566537cc;

  /// Flule34 UI: 例如：喜欢的动画、待整理
  ///
  /// In zh, this message translates to:
  /// **'例如：喜欢的动画、待整理'**
  String get ui65962099;

  /// Flule34 UI: 保存
  ///
  /// In zh, this message translates to:
  /// **'保存'**
  String get ui29629697;

  /// Flule34 UI: 保存搜索历史
  ///
  /// In zh, this message translates to:
  /// **'保存搜索历史'**
  String get ui76444c7d;

  /// Flule34 UI: 保存更新通道失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'保存更新通道失败：{p0}'**
  String ui4dc6233e(String p0);

  /// Flule34 UI: 保存翻译失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'保存翻译失败：{p0}'**
  String ui69df41e4(String p0);

  /// Flule34 UI: 保存翻译服务失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'保存翻译服务失败：{p0}'**
  String ui696410b7(String p0);

  /// Flule34 UI: 保存设置失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'保存设置失败：{p0}'**
  String ui3e44bdb9(String p0);

  /// Flule34 UI: 保持设备当前方向
  ///
  /// In zh, this message translates to:
  /// **'保持设备当前方向'**
  String get ui65d91d2b;

  /// Flule34 UI: 保留已经下载到公共目录的视频
  ///
  /// In zh, this message translates to:
  /// **'保留已经下载到公共目录的视频'**
  String get ui4f586a83;

  /// Flule34 UI: 修改密码
  ///
  /// In zh, this message translates to:
  /// **'修改密码'**
  String get ui30350f33;

  /// Flule34 UI: 修改邮箱
  ///
  /// In zh, this message translates to:
  /// **'修改邮箱'**
  String get ui043de786;

  /// Flule34 UI: 全屏
  ///
  /// In zh, this message translates to:
  /// **'全屏'**
  String get ui4fcf2a14;

  /// Flule34 UI: 全屏方向
  ///
  /// In zh, this message translates to:
  /// **'全屏方向'**
  String get ui784e54fd;

  /// Flule34 UI: 全部
  ///
  /// In zh, this message translates to:
  /// **'全部'**
  String get ui0e1cd927;

  /// Flule34 UI: 全部清除
  ///
  /// In zh, this message translates to:
  /// **'全部清除'**
  String get ui2a504352;

  /// Flule34 UI: 共 {p0} 个任务 · 已完成 {p1} 个 · 约占用 {p2}
  ///
  /// In zh, this message translates to:
  /// **'共 {p0} 个任务 · 已完成 {p1} 个 · 约占用 {p2}'**
  String ui78d96dee(String p0, String p1, String p2);

  /// Flule34 UI: 共 {p0} 条 · 内置 {p1} · API {p2} · 用户 {p3}
  ///
  /// In zh, this message translates to:
  /// **'共 {p0} 条 · 内置 {p1} · API {p2} · 用户 {p3}'**
  String ui3b4a622d(String p0, String p1, String p2, String p3);

  /// Flule34 UI: 关于 Flule34
  ///
  /// In zh, this message translates to:
  /// **'关于 Flule34'**
  String get ui166298c5;

  /// Flule34 UI: 关注
  ///
  /// In zh, this message translates to:
  /// **'关注'**
  String get ui13bc9fa5;

  /// Flule34 UI: 关注的分类、艺术家或用户暂时没有可展示的视频。
  ///
  /// In zh, this message translates to:
  /// **'关注的分类、艺术家或用户暂时没有可展示的视频。'**
  String get ui54d03562;

  /// Flule34 UI: 关注频道会汇总你在网站订阅的分类、艺术家、用户和播放列表。
  ///
  /// In zh, this message translates to:
  /// **'关注频道会汇总你在网站订阅的分类、艺术家、用户和播放列表。'**
  String get ui47de51e1;

  /// Flule34 UI: 关闭后将清除全部本地播放进度。
  ///
  /// In zh, this message translates to:
  /// **'关闭后将清除全部本地播放进度。'**
  String get ui29c40c72;

  /// Flule34 UI: 关闭并清除
  ///
  /// In zh, this message translates to:
  /// **'关闭并清除'**
  String get ui02e95068;

  /// Flule34 UI: 关闭记忆播放进度？
  ///
  /// In zh, this message translates to:
  /// **'关闭记忆播放进度？'**
  String get ui08354b81;

  /// Flule34 UI: 内容取向
  ///
  /// In zh, this message translates to:
  /// **'内容取向'**
  String get ui2bbc0423;

  /// Flule34 UI: 内容设置
  ///
  /// In zh, this message translates to:
  /// **'内容设置'**
  String get ui4804490f;

  /// Flule34 UI: 内置
  ///
  /// In zh, this message translates to:
  /// **'内置'**
  String get ui38d59e4d;

  /// Flule34 UI: 分享
  ///
  /// In zh, this message translates to:
  /// **'分享'**
  String get ui2f5fd7d1;

  /// Flule34 UI: 分类
  ///
  /// In zh, this message translates to:
  /// **'分类'**
  String get ui55599ffb;

  /// Flule34 UI: 列表循环
  ///
  /// In zh, this message translates to:
  /// **'列表循环'**
  String get ui38fe9b1d;

  /// Flule34 UI: 列表顺序
  ///
  /// In zh, this message translates to:
  /// **'列表顺序'**
  String get ui309e167e;

  /// Flule34 UI: 创建自定义分类后，可以从任意视频的“本地分类库”按钮保存到这里。
  ///
  /// In zh, this message translates to:
  /// **'创建自定义分类后，可以从任意视频的“本地分类库”按钮保存到这里。'**
  String get ui0c2c660a;

  /// Flule34 UI: 删除
  ///
  /// In zh, this message translates to:
  /// **'删除'**
  String get ui1ae0ab8e;

  /// Flule34 UI: 删除 API 译文
  ///
  /// In zh, this message translates to:
  /// **'删除 API 译文'**
  String get ui1cb9a6d7;

  /// Flule34 UI: 删除“{p0}”？
  ///
  /// In zh, this message translates to:
  /// **'删除“{p0}”？'**
  String ui2d23933f(String p0);

  /// Flule34 UI: 删除下载？
  ///
  /// In zh, this message translates to:
  /// **'删除下载？'**
  String get ui3913a7a5;

  /// Flule34 UI: 删除全部下载记录
  ///
  /// In zh, this message translates to:
  /// **'删除全部下载记录'**
  String get ui6beb71f2;

  /// Flule34 UI: 删除全部下载记录及对应视频
  ///
  /// In zh, this message translates to:
  /// **'删除全部下载记录及对应视频'**
  String get ui4e3e94a5;

  /// Flule34 UI: 删除全部下载记录，并删除公共目录中仍能对应上的视频。无法删除文件的记录会保留。
  ///
  /// In zh, this message translates to:
  /// **'删除全部下载记录，并删除公共目录中仍能对应上的视频。无法删除文件的记录会保留。'**
  String get ui32521bda;

  /// Flule34 UI: 删除全部失效下载记录
  ///
  /// In zh, this message translates to:
  /// **'删除全部失效下载记录'**
  String get ui499f4bf1;

  /// Flule34 UI: 删除全部已经找不到严格对应文件的下载记录，不会触碰外部文件。
  ///
  /// In zh, this message translates to:
  /// **'删除全部已经找不到严格对应文件的下载记录，不会触碰外部文件。'**
  String get ui7622d7c4;

  /// Flule34 UI: 删除所选 API 译文？
  ///
  /// In zh, this message translates to:
  /// **'删除所选 API 译文？'**
  String get ui42079bac;

  /// Flule34 UI: 删除文件和记录
  ///
  /// In zh, this message translates to:
  /// **'删除文件和记录'**
  String get ui6882566e;

  /// Flule34 UI: 删除翻译服务失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'删除翻译服务失败：{p0}'**
  String ui13dbc37c(String p0);

  /// Flule34 UI: 删除翻译服务？
  ///
  /// In zh, this message translates to:
  /// **'删除翻译服务？'**
  String get ui377546a6;

  /// Flule34 UI: 删除自定义翻译
  ///
  /// In zh, this message translates to:
  /// **'删除自定义翻译'**
  String get ui58aa0fc9;

  /// Flule34 UI: 删除这台设备上的全部应用日志。
  ///
  /// In zh, this message translates to:
  /// **'删除这台设备上的全部应用日志。'**
  String get ui59ee6b29;

  /// Flule34 UI: 刷新
  ///
  /// In zh, this message translates to:
  /// **'刷新'**
  String get ui057a59bf;

  /// Flule34 UI: 刷新后仍未找到可播放的视频源。
  ///
  /// In zh, this message translates to:
  /// **'刷新后仍未找到可播放的视频源。'**
  String get ui1a88cf99;

  /// Flule34 UI: 刷新后已找不到 {p0} 下载源。
  ///
  /// In zh, this message translates to:
  /// **'刷新后已找不到 {p0} 下载源。'**
  String ui30d8aa7b(String p0);

  /// Flule34 UI: 刷新后已找不到 {p0} 下载源，请重新选择清晰度。
  ///
  /// In zh, this message translates to:
  /// **'刷新后已找不到 {p0} 下载源，请重新选择清晰度。'**
  String ui1adad0d8(String p0);

  /// Flule34 UI: 刷新视频地址失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'刷新视频地址失败：{p0}'**
  String ui1b5c10c1(String p0);

  /// Flule34 UI: 加载下一视频失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'加载下一视频失败：{p0}'**
  String ui7050fd74(String p0);

  /// Flule34 UI: 加载视频失败。
  ///
  /// In zh, this message translates to:
  /// **'加载视频失败。'**
  String get ui11255e4d;

  /// Flule34 UI: 勾选需要自动翻译的内容类型；仅在缺少本地译文且已配置可用翻译服务时请求。默认全部关闭。
  ///
  /// In zh, this message translates to:
  /// **'勾选需要自动翻译的内容类型；仅在缺少本地译文且已配置可用翻译服务时请求。默认全部关闭。'**
  String get ui2fbeba49;

  /// Flule34 UI: 包名
  ///
  /// In zh, this message translates to:
  /// **'包名'**
  String get ui3caea101;

  /// Flule34 UI: 匹配译名：{p0}
  ///
  /// In zh, this message translates to:
  /// **'匹配译名：{p0}'**
  String ui3c554cab(String p0);

  /// Flule34 UI: 单集循环
  ///
  /// In zh, this message translates to:
  /// **'单集循环'**
  String get ui71c021b7;

  /// Flule34 UI: 历史
  ///
  /// In zh, this message translates to:
  /// **'历史'**
  String get ui1a330a72;

  /// Flule34 UI: 历史累计最高评分艺术家
  ///
  /// In zh, this message translates to:
  /// **'历史累计最高评分艺术家'**
  String get ui51fa37c2;

  /// Flule34 UI: 原文
  ///
  /// In zh, this message translates to:
  /// **'原文'**
  String get ui6ffe0a80;

  /// Flule34 UI: 双语
  ///
  /// In zh, this message translates to:
  /// **'双语'**
  String get ui54ec6c15;

  /// Flule34 UI: 发布时间
  ///
  /// In zh, this message translates to:
  /// **'发布时间'**
  String get ui2e2d0cb3;

  /// Flule34 UI: 发现
  ///
  /// In zh, this message translates to:
  /// **'发现'**
  String get ui0ccf8adf;

  /// Flule34 UI: 发现新版本 {p0}。
  ///
  /// In zh, this message translates to:
  /// **'发现新版本 {p0}。'**
  String ui0e705d18(String p0);

  /// Flule34 UI: 取向：{p0}
  ///
  /// In zh, this message translates to:
  /// **'取向：{p0}'**
  String ui07cfc2d2(String p0);

  /// Flule34 UI: 取消
  ///
  /// In zh, this message translates to:
  /// **'取消'**
  String get ui1cdb9be3;

  /// Flule34 UI: 取消收藏
  ///
  /// In zh, this message translates to:
  /// **'取消收藏'**
  String get ui0d684dfd;

  /// Flule34 UI: 取消订阅
  ///
  /// In zh, this message translates to:
  /// **'取消订阅'**
  String get ui5eb70fab;

  /// Flule34 UI: 取消选择
  ///
  /// In zh, this message translates to:
  /// **'取消选择'**
  String get ui78c52651;

  /// Flule34 UI: 另有 {p0} 条内置译文，仅用于审计，
  ///
  /// In zh, this message translates to:
  /// **'另有 {p0} 条内置译文，仅用于审计，'**
  String ui072ad981(String p0);

  /// Flule34 UI: 只会删除当前账号在这台设备上的搜索记录。此操作无法撤销。
  ///
  /// In zh, this message translates to:
  /// **'只会删除当前账号在这台设备上的搜索记录。此操作无法撤销。'**
  String get ui62d7fea9;

  /// Flule34 UI: 只会清除当前账号在这台设备上的搜索记录。
  ///
  /// In zh, this message translates to:
  /// **'只会清除当前账号在这台设备上的搜索记录。'**
  String get ui35027352;

  /// Flule34 UI: 只删除 App 中的全部下载记录，已经保存到 Download/Flule34 的视频会保留。进行中的任务会先取消。
  ///
  /// In zh, this message translates to:
  /// **'只删除 App 中的全部下载记录，已经保存到 Download/Flule34 的视频会保留。进行中的任务会先取消。'**
  String get ui73b35752;

  /// Flule34 UI: 只删除本地分类记录，不会删除网站收藏、历史或已下载的视频。
  ///
  /// In zh, this message translates to:
  /// **'只删除本地分类记录，不会删除网站收藏、历史或已下载的视频。'**
  String get ui5a6e7dac;

  /// Flule34 UI: 只移除已经找不到对应文件的记录
  ///
  /// In zh, this message translates to:
  /// **'只移除已经找不到对应文件的记录'**
  String get ui4f2368e4;

  /// Flule34 UI: 可以只移除 App 内记录，也可以尝试删除当前记录所指向的外部文件。
  ///
  /// In zh, this message translates to:
  /// **'可以只移除 App 内记录，也可以尝试删除当前记录所指向的外部文件。'**
  String get ui713b1fb0;

  /// Flule34 UI: 可跟随界面语言，也可单独指定；不同目标语言的译文会分别保存。
  ///
  /// In zh, this message translates to:
  /// **'可跟随界面语言，也可单独指定；不同目标语言的译文会分别保存。'**
  String get ui76ae23ba;

  /// Flule34 UI: 同性
  ///
  /// In zh, this message translates to:
  /// **'同性'**
  String get ui19e0d4bf;

  /// Flule34 UI: 同时下载任务数
  ///
  /// In zh, this message translates to:
  /// **'同时下载任务数'**
  String get ui2b2e17e5;

  /// Flule34 UI: 同时删除公共目录中仍能对应上的视频
  ///
  /// In zh, this message translates to:
  /// **'同时删除公共目录中仍能对应上的视频'**
  String get ui09e67cd1;

  /// Flule34 UI: 同类条件和不同类型条件均取交集，每类最多选择 5 项。
  ///
  /// In zh, this message translates to:
  /// **'同类条件和不同类型条件均取交集，每类最多选择 5 项。'**
  String get ui3898538c;

  /// Flule34 UI: 名称
  ///
  /// In zh, this message translates to:
  /// **'名称'**
  String get ui73f2614f;

  /// Flule34 UI: 后台任务进行中
  ///
  /// In zh, this message translates to:
  /// **'后台任务进行中'**
  String get ui3a38a6d4;

  /// Flule34 UI: 后台播放
  ///
  /// In zh, this message translates to:
  /// **'后台播放'**
  String get ui7f54b07b;

  /// Flule34 UI: 否
  ///
  /// In zh, this message translates to:
  /// **'否'**
  String get ui4763b5c2;

  /// Flule34 UI: 命中任一排除条件的视频不会显示
  ///
  /// In zh, this message translates to:
  /// **'命中任一排除条件的视频不会显示'**
  String get ui63f37124;

  /// Flule34 UI: 回到顶部
  ///
  /// In zh, this message translates to:
  /// **'回到顶部'**
  String get ui3791c2b8;

  /// Flule34 UI: 图片缓存已清除。
  ///
  /// In zh, this message translates to:
  /// **'图片缓存已清除。'**
  String get ui03a2a222;

  /// Flule34 UI: 在本机保存，与登录账号无关
  ///
  /// In zh, this message translates to:
  /// **'在本机保存，与登录账号无关'**
  String get ui796e3b4c;

  /// Flule34 UI: 在网站中修改头像、名称和公开资料
  ///
  /// In zh, this message translates to:
  /// **'在网站中修改头像、名称和公开资料'**
  String get ui12562321;

  /// Flule34 UI: 在网站中管理已上传的视频
  ///
  /// In zh, this message translates to:
  /// **'在网站中管理已上传的视频'**
  String get ui304779ae;

  /// Flule34 UI: 基址
  ///
  /// In zh, this message translates to:
  /// **'基址'**
  String get ui1f55def5;

  /// Flule34 UI: 基础条件
  ///
  /// In zh, this message translates to:
  /// **'基础条件'**
  String get ui6bdfd846;

  /// Flule34 UI: 复制
  ///
  /// In zh, this message translates to:
  /// **'复制'**
  String get ui461541d8;

  /// Flule34 UI: 复制版本、设备和配置摘要，不包含 Cookie 或密码
  ///
  /// In zh, this message translates to:
  /// **'复制版本、设备和配置摘要，不包含 Cookie 或密码'**
  String get ui5dd6981a;

  /// Flule34 UI: 复制翻译服务失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'复制翻译服务失败：{p0}'**
  String ui61570e3e(String p0);

  /// Flule34 UI: 复制诊断信息
  ///
  /// In zh, this message translates to:
  /// **'复制诊断信息'**
  String get ui0ca5a4ba;

  /// Flule34 UI: 外部文件大小已发生变化。
  ///
  /// In zh, this message translates to:
  /// **'外部文件大小已发生变化。'**
  String get ui2a4866c9;

  /// Flule34 UI: 外部文件已不存在。
  ///
  /// In zh, this message translates to:
  /// **'外部文件已不存在。'**
  String get ui46887217;

  /// Flule34 UI: 外部文件已被改名。
  ///
  /// In zh, this message translates to:
  /// **'外部文件已被改名。'**
  String get ui510839e9;

  /// Flule34 UI: 外部文件当前无法读取。
  ///
  /// In zh, this message translates to:
  /// **'外部文件当前无法读取。'**
  String get ui3be928a0;

  /// Flule34 UI: 始终使用默认清晰度
  ///
  /// In zh, this message translates to:
  /// **'始终使用默认清晰度'**
  String get ui158640ea;

  /// Flule34 UI: 媒体库
  ///
  /// In zh, this message translates to:
  /// **'媒体库'**
  String get ui17588e00;

  /// Flule34 UI: 存在
  ///
  /// In zh, this message translates to:
  /// **'存在'**
  String get ui344971fc;

  /// Flule34 UI: 安全合并
  ///
  /// In zh, this message translates to:
  /// **'安全合并'**
  String get ui60514b78;

  /// Flule34 UI: 密码
  ///
  /// In zh, this message translates to:
  /// **'密码'**
  String get ui5baf4155;

  /// Flule34 UI: 导入失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'导入失败：{p0}'**
  String ui65cceef6(String p0);

  /// Flule34 UI: 导入或导出
  ///
  /// In zh, this message translates to:
  /// **'导入或导出'**
  String get ui4181e94a;

  /// Flule34 UI: 导入文件优先
  ///
  /// In zh, this message translates to:
  /// **'导入文件优先'**
  String get ui347e69e0;

  /// Flule34 UI: 导入时会忽略。请选择冲突处理方式。
  ///
  /// In zh, this message translates to:
  /// **'导入时会忽略。请选择冲突处理方式。'**
  String get ui7b8b8627;

  /// Flule34 UI: 导入翻译库
  ///
  /// In zh, this message translates to:
  /// **'导入翻译库'**
  String get ui3447243f;

  /// Flule34 UI: 导出日志
  ///
  /// In zh, this message translates to:
  /// **'导出日志'**
  String get ui29108110;

  /// Flule34 UI: 导出日志失败，请稍后重试。
  ///
  /// In zh, this message translates to:
  /// **'导出日志失败，请稍后重试。'**
  String get ui561390c3;

  /// Flule34 UI: 导出时间：{p0}
  ///
  /// In zh, this message translates to:
  /// **'导出时间：{p0}'**
  String ui4bddfd15(String p0);

  /// Flule34 UI: 导出翻译库
  ///
  /// In zh, this message translates to:
  /// **'导出翻译库'**
  String get ui1a3a31c6;

  /// Flule34 UI: 导出翻译库失败。
  ///
  /// In zh, this message translates to:
  /// **'导出翻译库失败。'**
  String get ui2d28ccb0;

  /// Flule34 UI: 将删除“{p0}”及其本机密钥。
  ///
  /// In zh, this message translates to:
  /// **'将删除“{p0}”及其本机密钥。'**
  String ui0d4b5d1d(String p0);

  /// Flule34 UI: 将删除本机保存的账号、密码和登录会话；设备下载与本地分类库不会受影响。
  ///
  /// In zh, this message translates to:
  /// **'将删除本机保存的账号、密码和登录会话；设备下载与本地分类库不会受影响。'**
  String get ui5116cc17;

  /// Flule34 UI: 将删除这台设备上的全部诊断日志，此操作无法撤销。
  ///
  /// In zh, this message translates to:
  /// **'将删除这台设备上的全部诊断日志，此操作无法撤销。'**
  String get ui206e15fd;

  /// Flule34 UI: 将永久删除 {p0} 条 API 译文。用户手动译文和内置译文不会被删除。
  ///
  /// In zh, this message translates to:
  /// **'将永久删除 {p0} 条 API 译文。用户手动译文和内置译文不会被删除。'**
  String ui61998fc7(String p0);

  /// Flule34 UI: 尚未登录
  ///
  /// In zh, this message translates to:
  /// **'尚未登录'**
  String get ui2d851aa0;

  /// Flule34 UI: 尚未选择{p0}
  ///
  /// In zh, this message translates to:
  /// **'尚未选择{p0}'**
  String ui5a665aac(String p0);

  /// Flule34 UI: 尚未配置翻译服务。内置词表和用户手动译文仍可正常使用。
  ///
  /// In zh, this message translates to:
  /// **'尚未配置翻译服务。内置词表和用户手动译文仍可正常使用。'**
  String get ui7d437796;

  /// Flule34 UI: 已下载
  ///
  /// In zh, this message translates to:
  /// **'已下载'**
  String get ui0543d520;

  /// Flule34 UI: 已从“{p0}”移出。
  ///
  /// In zh, this message translates to:
  /// **'已从“{p0}”移出。'**
  String ui4c1b3a95(String p0);

  /// Flule34 UI: 已从播放列表“{p0}”移出。
  ///
  /// In zh, this message translates to:
  /// **'已从播放列表“{p0}”移出。'**
  String ui228152d7(String p0);

  /// Flule34 UI: 已从播放列表移出。
  ///
  /// In zh, this message translates to:
  /// **'已从播放列表移出。'**
  String get ui1fa11a46;

  /// Flule34 UI: 已从本地库移出。
  ///
  /// In zh, this message translates to:
  /// **'已从本地库移出。'**
  String get ui64769355;

  /// Flule34 UI: 已关闭
  ///
  /// In zh, this message translates to:
  /// **'已关闭'**
  String get ui55781737;

  /// Flule34 UI: 已删除 {p0} 条下载记录。
  ///
  /// In zh, this message translates to:
  /// **'已删除 {p0} 条下载记录。'**
  String ui69dc1173(String p0);

  /// Flule34 UI: 已删除 {p0} 条，{p1} 条未能删除。
  ///
  /// In zh, this message translates to:
  /// **'已删除 {p0} 条，{p1} 条未能删除。'**
  String ui5ed2011c(String p0, String p1);

  /// Flule34 UI: 已加入“{p0}”。
  ///
  /// In zh, this message translates to:
  /// **'已加入“{p0}”。'**
  String ui5846e503(String p0);

  /// Flule34 UI: 已加入播放列表“{p0}”。
  ///
  /// In zh, this message translates to:
  /// **'已加入播放列表“{p0}”。'**
  String ui6b12697d(String p0);

  /// Flule34 UI: 已加入收藏。
  ///
  /// In zh, this message translates to:
  /// **'已加入收藏。'**
  String get ui670889d8;

  /// Flule34 UI: 已取消
  ///
  /// In zh, this message translates to:
  /// **'已取消'**
  String get ui37453e63;

  /// Flule34 UI: 已取消收藏。
  ///
  /// In zh, this message translates to:
  /// **'已取消收藏。'**
  String get ui7bbd0e24;

  /// Flule34 UI: 已取消订阅。
  ///
  /// In zh, this message translates to:
  /// **'已取消订阅。'**
  String get ui34a0e3be;

  /// Flule34 UI: 已学习标题 · {p0}
  ///
  /// In zh, this message translates to:
  /// **'已学习标题 · {p0}'**
  String ui1db0bde1(String p0);

  /// Flule34 UI: 已导入 {p0} 层译文
  ///
  /// In zh, this message translates to:
  /// **'已导入 {p0} 层译文'**
  String ui7a8ce229(String p0);

  /// Flule34 UI: 已开启
  ///
  /// In zh, this message translates to:
  /// **'已开启'**
  String get ui0de2ecda;

  /// Flule34 UI: 已收藏
  ///
  /// In zh, this message translates to:
  /// **'已收藏'**
  String get ui0077d937;

  /// Flule34 UI: 已新建并加入播放列表“{p0}”。
  ///
  /// In zh, this message translates to:
  /// **'已新建并加入播放列表“{p0}”。'**
  String ui2ce07361(String p0);

  /// Flule34 UI: 已暂停
  ///
  /// In zh, this message translates to:
  /// **'已暂停'**
  String get ui1a7827b1;

  /// Flule34 UI: 已经到底了
  ///
  /// In zh, this message translates to:
  /// **'已经到底了'**
  String get ui49531ef1;

  /// Flule34 UI: 已经存在同名的本地库。
  ///
  /// In zh, this message translates to:
  /// **'已经存在同名的本地库。'**
  String get ui15a96bf1;

  /// Flule34 UI: 已经是播放列表最后一个视频。
  ///
  /// In zh, this message translates to:
  /// **'已经是播放列表最后一个视频。'**
  String get ui69288ef8;

  /// Flule34 UI: 已订阅
  ///
  /// In zh, this message translates to:
  /// **'已订阅'**
  String get ui24d4c17d;

  /// Flule34 UI: 已订阅。
  ///
  /// In zh, this message translates to:
  /// **'已订阅。'**
  String get ui426dc524;

  /// Flule34 UI: 已订阅上传者。
  ///
  /// In zh, this message translates to:
  /// **'已订阅上传者。'**
  String get ui59a2ec21;

  /// Flule34 UI: 已选择 {p0} 项
  ///
  /// In zh, this message translates to:
  /// **'已选择 {p0} 项'**
  String ui21a8fcc4(String p0);

  /// Flule34 UI: 已重新加入下载队列。
  ///
  /// In zh, this message translates to:
  /// **'已重新加入下载队列。'**
  String get ui538facf2;

  /// Flule34 UI: 已验证上传者
  ///
  /// In zh, this message translates to:
  /// **'已验证上传者'**
  String get ui1d982807;

  /// Flule34 UI: 帮助与反馈
  ///
  /// In zh, this message translates to:
  /// **'帮助与反馈'**
  String get ui563d1236;

  /// Flule34 UI: 平台
  ///
  /// In zh, this message translates to:
  /// **'平台'**
  String get ui62a81a58;

  /// Flule34 UI: 库名称
  ///
  /// In zh, this message translates to:
  /// **'库名称'**
  String get ui70131201;

  /// Flule34 UI: 库名称不能为空。
  ///
  /// In zh, this message translates to:
  /// **'库名称不能为空。'**
  String get ui14bf4ac7;

  /// Flule34 UI: 应用
  ///
  /// In zh, this message translates to:
  /// **'应用'**
  String get ui643b8cff;

  /// Flule34 UI: 应用 {p0} 个条件
  ///
  /// In zh, this message translates to:
  /// **'应用 {p0} 个条件'**
  String ui7be16f02(String p0);

  /// Flule34 UI: 应用初始化完成。
  ///
  /// In zh, this message translates to:
  /// **'应用初始化完成。'**
  String get ui103ff6bd;

  /// Flule34 UI: 应用日志
  ///
  /// In zh, this message translates to:
  /// **'应用日志'**
  String get ui75af3770;

  /// Flule34 UI: 应用日志已清除。
  ///
  /// In zh, this message translates to:
  /// **'应用日志已清除。'**
  String get ui38f27f7a;

  /// Flule34 UI: 应用（不限）
  ///
  /// In zh, this message translates to:
  /// **'应用（不限）'**
  String get ui390d6cf3;

  /// Flule34 UI: 开启后，切换应用或关闭屏幕时继续播放声音。
  ///
  /// In zh, this message translates to:
  /// **'开启后，切换应用或关闭屏幕时继续播放声音。'**
  String get ui0a663237;

  /// Flule34 UI: 开源许可
  ///
  /// In zh, this message translates to:
  /// **'开源许可'**
  String get ui13034753;

  /// Flule34 UI: 异性
  ///
  /// In zh, this message translates to:
  /// **'异性'**
  String get ui1fbbcc39;

  /// Flule34 UI: 当前任务会先被取消。你可以只删除记录，也可以同时清理未完成文件。
  ///
  /// In zh, this message translates to:
  /// **'当前任务会先被取消。你可以只删除记录，也可以同时清理未完成文件。'**
  String get ui573acdd9;

  /// Flule34 UI: 当前已加载内容没有匹配项。
  ///
  /// In zh, this message translates to:
  /// **'当前已加载内容没有匹配项。'**
  String get ui3c131161;

  /// Flule34 UI: 当前已是最新版本。
  ///
  /// In zh, this message translates to:
  /// **'当前已是最新版本。'**
  String get ui73c532ff;

  /// Flule34 UI: 当前开发构建未配置更新源
  ///
  /// In zh, this message translates to:
  /// **'当前开发构建未配置更新源'**
  String get ui34a6f44b;

  /// Flule34 UI: 当前开发构建未配置更新源。
  ///
  /// In zh, this message translates to:
  /// **'当前开发构建未配置更新源。'**
  String get ui2c29265e;

  /// Flule34 UI: 当前未登录
  ///
  /// In zh, this message translates to:
  /// **'当前未登录'**
  String get ui309047a5;

  /// Flule34 UI: 当前构建未配置仓库地址
  ///
  /// In zh, this message translates to:
  /// **'当前构建未配置仓库地址'**
  String get ui5cc85dd9;

  /// Flule34 UI: 当前版本：{p0}
  ///
  /// In zh, this message translates to:
  /// **'当前版本：{p0}'**
  String ui34dcc5aa(String p0);

  /// Flule34 UI: 当前账号 ID
  ///
  /// In zh, this message translates to:
  /// **'当前账号 ID'**
  String get ui1ef7e413;

  /// Flule34 UI: 循环播放
  ///
  /// In zh, this message translates to:
  /// **'循环播放'**
  String get ui4f25fec3;

  /// Flule34 UI: 必须同时包含
  ///
  /// In zh, this message translates to:
  /// **'必须同时包含'**
  String get ui761f6d4f;

  /// Flule34 UI: 忘记密码
  ///
  /// In zh, this message translates to:
  /// **'忘记密码'**
  String get ui5362cf1f;

  /// Flule34 UI: 忽略内置 {p0}。
  ///
  /// In zh, this message translates to:
  /// **'忽略内置 {p0}。'**
  String ui13e52148(String p0);

  /// Flule34 UI: 恢复内置翻译
  ///
  /// In zh, this message translates to:
  /// **'恢复内置翻译'**
  String get ui1f9121af;

  /// Flule34 UI: 恢复已学习翻译
  ///
  /// In zh, this message translates to:
  /// **'恢复已学习翻译'**
  String get ui608e380c;

  /// Flule34 UI: 我的
  ///
  /// In zh, this message translates to:
  /// **'我的'**
  String get ui67d3b06d;

  /// Flule34 UI: 我的上传
  ///
  /// In zh, this message translates to:
  /// **'我的上传'**
  String get ui1065acd3;

  /// Flule34 UI: 所有网络都使用上方选择的清晰度
  ///
  /// In zh, this message translates to:
  /// **'所有网络都使用上方选择的清晰度'**
  String get ui3ae6be59;

  /// Flule34 UI: 所选本地库已经不存在。
  ///
  /// In zh, this message translates to:
  /// **'所选本地库已经不存在。'**
  String get ui2274fd3b;

  /// Flule34 UI: 打开 GitHub 发布页
  ///
  /// In zh, this message translates to:
  /// **'打开 GitHub 发布页'**
  String get ui6fa5a093;

  /// Flule34 UI: 打开{p0}集合
  ///
  /// In zh, this message translates to:
  /// **'打开{p0}集合'**
  String ui6ae92059(String p0);

  /// Flule34 UI: 打开下载失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'打开下载失败：{p0}'**
  String ui580f715d(String p0);

  /// Flule34 UI: 打开官方网站
  ///
  /// In zh, this message translates to:
  /// **'打开官方网站'**
  String get ui02a64714;

  /// Flule34 UI: 打开网站反馈表单
  ///
  /// In zh, this message translates to:
  /// **'打开网站反馈表单'**
  String get ui0d472be2;

  /// Flule34 UI: 打开网站消息中心
  ///
  /// In zh, this message translates to:
  /// **'打开网站消息中心'**
  String get ui0fb6d05e;

  /// Flule34 UI: 扶她
  ///
  /// In zh, this message translates to:
  /// **'扶她'**
  String get ui5c30a6ab;

  /// Flule34 UI: 批量删除
  ///
  /// In zh, this message translates to:
  /// **'批量删除'**
  String get ui52437893;

  /// Flule34 UI: 投票数 ≥ {p0}
  ///
  /// In zh, this message translates to:
  /// **'投票数 ≥ {p0}'**
  String ui41bd594d(String p0);

  /// Flule34 UI: 报告不包含 Cookie、密码、邮箱、用户 ID 值或 Android 设备标识符。发送前仍建议自行检查。
  ///
  /// In zh, this message translates to:
  /// **'报告不包含 Cookie、密码、邮箱、用户 ID 值或 Android 设备标识符。发送前仍建议自行检查。'**
  String get ui7069486d;

  /// Flule34 UI: 拉取模型列表
  ///
  /// In zh, this message translates to:
  /// **'拉取模型列表'**
  String get ui7d6a579d;

  /// Flule34 UI: 按原文排序
  ///
  /// In zh, this message translates to:
  /// **'按原文排序'**
  String get ui65af3a45;

  /// Flule34 UI: 按名字
  ///
  /// In zh, this message translates to:
  /// **'按名字'**
  String get ui55e84e41;

  /// Flule34 UI: 按最近更新排序
  ///
  /// In zh, this message translates to:
  /// **'按最近更新排序'**
  String get ui384e319d;

  /// Flule34 UI: 按来源排序
  ///
  /// In zh, this message translates to:
  /// **'按来源排序'**
  String get ui7ab117f8;

  /// Flule34 UI: 按标签和内容主题探索
  ///
  /// In zh, this message translates to:
  /// **'按标签和内容主题探索'**
  String get ui70c4de19;

  /// Flule34 UI: 按观看量浏览热门内容
  ///
  /// In zh, this message translates to:
  /// **'按观看量浏览热门内容'**
  String get ui0db93df0;

  /// Flule34 UI: 按译文排序
  ///
  /// In zh, this message translates to:
  /// **'按译文排序'**
  String get ui05f1a141;

  /// Flule34 UI: 排序
  ///
  /// In zh, this message translates to:
  /// **'排序'**
  String get ui4f8317d3;

  /// Flule34 UI: 排序：{p0}
  ///
  /// In zh, this message translates to:
  /// **'排序：{p0}'**
  String ui702bc146(String p0);

  /// Flule34 UI: 排行榜
  ///
  /// In zh, this message translates to:
  /// **'排行榜'**
  String get ui6b955ece;

  /// Flule34 UI: 排除
  ///
  /// In zh, this message translates to:
  /// **'排除'**
  String get ui077c6159;

  /// Flule34 UI: 排除内容
  ///
  /// In zh, this message translates to:
  /// **'排除内容'**
  String get ui20d42365;

  /// Flule34 UI: 排除：
  ///
  /// In zh, this message translates to:
  /// **'排除：'**
  String get ui549d6c00;

  /// Flule34 UI: 探索内容
  ///
  /// In zh, this message translates to:
  /// **'探索内容'**
  String get ui3cca6594;

  /// Flule34 UI: 接口类型
  ///
  /// In zh, this message translates to:
  /// **'接口类型'**
  String get ui6ec4c172;

  /// Flule34 UI: 接口类型或服务器已改变，请重新填写密钥
  ///
  /// In zh, this message translates to:
  /// **'接口类型或服务器已改变，请重新填写密钥'**
  String get ui7daaecfb;

  /// Flule34 UI: 描述（可选）
  ///
  /// In zh, this message translates to:
  /// **'描述（可选）'**
  String get ui4aa4bf66;

  /// Flule34 UI: 提交后台下载任务失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'提交后台下载任务失败：{p0}'**
  String ui0c0bc8f8(String p0);

  /// Flule34 UI: 提示：长按标题、分类或标签，可以手动添加或修改译文。
  ///
  /// In zh, this message translates to:
  /// **'提示：长按标题、分类或标签，可以手动添加或修改译文。'**
  String get ui48d043db;

  /// Flule34 UI: 搜索
  ///
  /// In zh, this message translates to:
  /// **'搜索'**
  String get ui7365d58c;

  /// Flule34 UI: 搜索{p0}
  ///
  /// In zh, this message translates to:
  /// **'搜索{p0}'**
  String ui0726d620(String p0);

  /// Flule34 UI: 搜索全部{p0}
  ///
  /// In zh, this message translates to:
  /// **'搜索全部{p0}'**
  String ui35022cd6(String p0);

  /// Flule34 UI: 搜索历史
  ///
  /// In zh, this message translates to:
  /// **'搜索历史'**
  String get ui72dba787;

  /// Flule34 UI: 搜索历史已清除。
  ///
  /// In zh, this message translates to:
  /// **'搜索历史已清除。'**
  String get ui60e69fcd;

  /// Flule34 UI: 搜索历史清空失败，请稍后重试。
  ///
  /// In zh, this message translates to:
  /// **'搜索历史清空失败，请稍后重试。'**
  String get ui7dd406e9;

  /// Flule34 UI: 搜索原文、译文或翻译服务
  ///
  /// In zh, this message translates to:
  /// **'搜索原文、译文或翻译服务'**
  String get ui358b0b68;

  /// Flule34 UI: 搜索已加载的视频
  ///
  /// In zh, this message translates to:
  /// **'搜索已加载的视频'**
  String get ui6e169d07;

  /// Flule34 UI: 搜索成功，但历史记录保存失败。
  ///
  /// In zh, this message translates to:
  /// **'搜索成功，但历史记录保存失败。'**
  String get ui66473d1e;

  /// Flule34 UI: 搜索播放列表
  ///
  /// In zh, this message translates to:
  /// **'搜索播放列表'**
  String get ui7f749006;

  /// Flule34 UI: 搜索播放列表中的视频
  ///
  /// In zh, this message translates to:
  /// **'搜索播放列表中的视频'**
  String get ui6d63717d;

  /// Flule34 UI: 搜索收藏的视频
  ///
  /// In zh, this message translates to:
  /// **'搜索收藏的视频'**
  String get ui105d8758;

  /// Flule34 UI: 搜索本地库
  ///
  /// In zh, this message translates to:
  /// **'搜索本地库'**
  String get ui7d976e17;

  /// Flule34 UI: 搜索此库中的视频
  ///
  /// In zh, this message translates to:
  /// **'搜索此库中的视频'**
  String get ui342ff046;

  /// Flule34 UI: 搜索此订阅中的视频
  ///
  /// In zh, this message translates to:
  /// **'搜索此订阅中的视频'**
  String get ui6cb88a74;

  /// Flule34 UI: 搜索观看历史
  ///
  /// In zh, this message translates to:
  /// **'搜索观看历史'**
  String get ui35231688;

  /// Flule34 UI: 搜索视频、标签、分类或艺术家
  ///
  /// In zh, this message translates to:
  /// **'搜索视频、标签、分类或艺术家'**
  String get ui0e1e2e67;

  /// Flule34 UI: 搜索订阅
  ///
  /// In zh, this message translates to:
  /// **'搜索订阅'**
  String get ui49f810e0;

  /// Flule34 UI: 搜索记录删除失败，请稍后重试。
  ///
  /// In zh, this message translates to:
  /// **'搜索记录删除失败，请稍后重试。'**
  String get ui761a4e53;

  /// Flule34 UI: 撤销自定义
  ///
  /// In zh, this message translates to:
  /// **'撤销自定义'**
  String get ui645e5e1c;

  /// Flule34 UI: 播放
  ///
  /// In zh, this message translates to:
  /// **'播放'**
  String get ui73d23748;

  /// Flule34 UI: 播放列表
  ///
  /// In zh, this message translates to:
  /// **'播放列表'**
  String get ui16f3ad93;

  /// Flule34 UI: 播放列表 {p0}
  ///
  /// In zh, this message translates to:
  /// **'播放列表 {p0}'**
  String ui2189de41(String p0);

  /// Flule34 UI: 播放列表会从网站账号中删除。
  ///
  /// In zh, this message translates to:
  /// **'播放列表会从网站账号中删除。'**
  String get ui264bb7d8;

  /// Flule34 UI: 播放列表已创建。
  ///
  /// In zh, this message translates to:
  /// **'播放列表已创建。'**
  String get ui1f1bcb06;

  /// Flule34 UI: 播放列表已创建，但未能读取新列表。
  ///
  /// In zh, this message translates to:
  /// **'播放列表已创建，但未能读取新列表。'**
  String get ui32c513bd;

  /// Flule34 UI: 播放列表已删除。
  ///
  /// In zh, this message translates to:
  /// **'播放列表已删除。'**
  String get ui080bbabb;

  /// Flule34 UI: 播放列表已更新。
  ///
  /// In zh, this message translates to:
  /// **'播放列表已更新。'**
  String get ui49fa8b9b;

  /// Flule34 UI: 播放列表播放参数无效。
  ///
  /// In zh, this message translates to:
  /// **'播放列表播放参数无效。'**
  String get ui5ba71ce6;

  /// Flule34 UI: 播放器初始化后未提供视频时长。
  ///
  /// In zh, this message translates to:
  /// **'播放器初始化后未提供视频时长。'**
  String get ui7e8be483;

  /// Flule34 UI: 播放文件
  ///
  /// In zh, this message translates to:
  /// **'播放文件'**
  String get ui206c2436;

  /// Flule34 UI: 播放时保持屏幕常亮
  ///
  /// In zh, this message translates to:
  /// **'播放时保持屏幕常亮'**
  String get ui46f59caf;

  /// Flule34 UI: 播放清晰度
  ///
  /// In zh, this message translates to:
  /// **'播放清晰度'**
  String get ui1c97d427;

  /// Flule34 UI: 播放源失效时 App 会重新请求视频详情。仍无法播放时，请复制诊断信息并在反馈中说明视频链接和清晰度。
  ///
  /// In zh, this message translates to:
  /// **'播放源失效时 App 会重新请求视频详情。仍无法播放时，请复制诊断信息并在反馈中说明视频链接和清晰度。'**
  String get ui3940d7b7;

  /// Flule34 UI: 播放设置
  ///
  /// In zh, this message translates to:
  /// **'播放设置'**
  String get ui03f9adce;

  /// Flule34 UI: 播放速度
  ///
  /// In zh, this message translates to:
  /// **'播放速度'**
  String get ui5caccc11;

  /// Flule34 UI: 播放问题
  ///
  /// In zh, this message translates to:
  /// **'播放问题'**
  String get ui21658def;

  /// Flule34 UI: 操作未能完成，请稍后重试。
  ///
  /// In zh, this message translates to:
  /// **'操作未能完成，请稍后重试。'**
  String get ui31d7af87;

  /// Flule34 UI: 收藏
  ///
  /// In zh, this message translates to:
  /// **'收藏'**
  String get ui0d933ab7;

  /// Flule34 UI: 收藏夹里还没有视频。
  ///
  /// In zh, this message translates to:
  /// **'收藏夹里还没有视频。'**
  String get ui60768862;

  /// Flule34 UI: 收藏状态读取失败，点击重试
  ///
  /// In zh, this message translates to:
  /// **'收藏状态读取失败，点击重试'**
  String get ui00b01c4f;

  /// Flule34 UI: 数据库结构
  ///
  /// In zh, this message translates to:
  /// **'数据库结构'**
  String get ui053602da;

  /// Flule34 UI: 文件不存在
  ///
  /// In zh, this message translates to:
  /// **'文件不存在'**
  String get ui1ce03cf7;

  /// Flule34 UI: 文件包含 API 译文 {p0} 条、
  ///
  /// In zh, this message translates to:
  /// **'文件包含 API 译文 {p0} 条、'**
  String ui37efec5c(String p0);

  /// Flule34 UI: 新建
  ///
  /// In zh, this message translates to:
  /// **'新建'**
  String get ui17e77337;

  /// Flule34 UI: 新建任务会等待符合条件的网络；已存在任务不被追溯修改。
  ///
  /// In zh, this message translates to:
  /// **'新建任务会等待符合条件的网络；已存在任务不被追溯修改。'**
  String get ui1b46740e;

  /// Flule34 UI: 新建播放列表
  ///
  /// In zh, this message translates to:
  /// **'新建播放列表'**
  String get ui1062b8a1;

  /// Flule34 UI: 新建本地库
  ///
  /// In zh, this message translates to:
  /// **'新建本地库'**
  String get ui264c8716;

  /// Flule34 UI: 新建翻译服务
  ///
  /// In zh, this message translates to:
  /// **'新建翻译服务'**
  String get ui742da263;

  /// Flule34 UI: 无法将视频保存到 Download/Flule34。
  ///
  /// In zh, this message translates to:
  /// **'无法将视频保存到 Download/Flule34。'**
  String get ui3180d36c;

  /// Flule34 UI: 无法打开分享面板：{p0}
  ///
  /// In zh, this message translates to:
  /// **'无法打开分享面板：{p0}'**
  String ui180bd386(String p0);

  /// Flule34 UI: 无法播放此视频源：{p0}
  ///
  /// In zh, this message translates to:
  /// **'无法播放此视频源：{p0}'**
  String ui3a33698e(String p0);

  /// Flule34 UI: 无法生成诊断信息：{p0}
  ///
  /// In zh, this message translates to:
  /// **'无法生成诊断信息：{p0}'**
  String ui310db05f(String p0);

  /// Flule34 UI: 无法连接 GitHub，请检查网络后重试。
  ///
  /// In zh, this message translates to:
  /// **'无法连接 GitHub，请检查网络后重试。'**
  String get ui0b6ddbbb;

  /// Flule34 UI: 日本語
  ///
  /// In zh, this message translates to:
  /// **'日本語'**
  String get ui005f5ce7;

  /// Flule34 UI: 旧版自定义端点
  ///
  /// In zh, this message translates to:
  /// **'旧版自定义端点'**
  String get ui60361df0;

  /// Flule34 UI: 时长
  ///
  /// In zh, this message translates to:
  /// **'时长'**
  String get ui3754e1ab;

  /// Flule34 UI: 时长最长
  ///
  /// In zh, this message translates to:
  /// **'时长最长'**
  String get ui194644ca;

  /// Flule34 UI: 是
  ///
  /// In zh, this message translates to:
  /// **'是'**
  String get ui16b646f4;

  /// Flule34 UI: 显示密码
  ///
  /// In zh, this message translates to:
  /// **'显示密码'**
  String get ui6a379702;

  /// Flule34 UI: 显示设置
  ///
  /// In zh, this message translates to:
  /// **'显示设置'**
  String get ui5e0f4440;

  /// Flule34 UI: 暂停
  ///
  /// In zh, this message translates to:
  /// **'暂停'**
  String get ui7b1cd931;

  /// Flule34 UI: 暂时无法检查更新，请稍后重试。
  ///
  /// In zh, this message translates to:
  /// **'暂时无法检查更新，请稍后重试。'**
  String get ui585c23ff;

  /// Flule34 UI: 暂时无法预览
  ///
  /// In zh, this message translates to:
  /// **'暂时无法预览'**
  String get ui47bde52d;

  /// Flule34 UI: 暂时没有可展示的热门标签。
  ///
  /// In zh, this message translates to:
  /// **'暂时没有可展示的热门标签。'**
  String get ui2effb403;

  /// Flule34 UI: 更多操作
  ///
  /// In zh, this message translates to:
  /// **'更多操作'**
  String get ui38e45090;

  /// Flule34 UI: 更新检查已完成。
  ///
  /// In zh, this message translates to:
  /// **'更新检查已完成。'**
  String get ui2ec2c481;

  /// Flule34 UI: 更新源
  ///
  /// In zh, this message translates to:
  /// **'更新源'**
  String get ui17e1bbfa;

  /// Flule34 UI: 更新源没有可用的 Android Release。
  ///
  /// In zh, this message translates to:
  /// **'更新源没有可用的 Android Release。'**
  String get ui0beabc18;

  /// Flule34 UI: 更新源：{p0}
  ///
  /// In zh, this message translates to:
  /// **'更新源：{p0}'**
  String ui55d54121(String p0);

  /// Flule34 UI: 更新通道
  ///
  /// In zh, this message translates to:
  /// **'更新通道'**
  String get ui1d030a86;

  /// Flule34 UI: 最低投票数
  ///
  /// In zh, this message translates to:
  /// **'最低投票数'**
  String get ui69112ae8;

  /// Flule34 UI: 最低点赞率
  ///
  /// In zh, this message translates to:
  /// **'最低点赞率'**
  String get ui65f28853;

  /// Flule34 UI: 最低票数
  ///
  /// In zh, this message translates to:
  /// **'最低票数'**
  String get ui51a023ab;

  /// Flule34 UI: 最多观看
  ///
  /// In zh, this message translates to:
  /// **'最多观看'**
  String get ui2b705f61;

  /// Flule34 UI: 最新
  ///
  /// In zh, this message translates to:
  /// **'最新'**
  String get ui347c998f;

  /// Flule34 UI: 最新创建
  ///
  /// In zh, this message translates to:
  /// **'最新创建'**
  String get ui222ba90b;

  /// Flule34 UI: 最新订阅
  ///
  /// In zh, this message translates to:
  /// **'最新订阅'**
  String get ui368db057;

  /// Flule34 UI: 最近修改
  ///
  /// In zh, this message translates to:
  /// **'最近修改'**
  String get ui23dfffd1;

  /// Flule34 UI: 最近更新
  ///
  /// In zh, this message translates to:
  /// **'最近更新'**
  String get ui6da2840c;

  /// Flule34 UI: 最近添加
  ///
  /// In zh, this message translates to:
  /// **'最近添加'**
  String get ui5891390e;

  /// Flule34 UI: 最长
  ///
  /// In zh, this message translates to:
  /// **'最长'**
  String get ui3f66748c;

  /// Flule34 UI: 最高可用
  ///
  /// In zh, this message translates to:
  /// **'最高可用'**
  String get ui72d8c6d5;

  /// Flule34 UI: 最高评分
  ///
  /// In zh, this message translates to:
  /// **'最高评分'**
  String get ui646cc4af;

  /// Flule34 UI: 服务名称
  ///
  /// In zh, this message translates to:
  /// **'服务名称'**
  String get ui7ee4b38a;

  /// Flule34 UI: 未捕获异步异常：{p0}
  /// {p1}
  ///
  /// In zh, this message translates to:
  /// **'未捕获异步异常：{p0}\n{p1}'**
  String ui5801f5b9(String p0, String p1);

  /// Flule34 UI: 未排除任何{p0}
  ///
  /// In zh, this message translates to:
  /// **'未排除任何{p0}'**
  String ui1d2649c7(String p0);

  /// Flule34 UI: 未配置
  ///
  /// In zh, this message translates to:
  /// **'未配置'**
  String get ui73b71caa;

  /// Flule34 UI: 本地分类库
  ///
  /// In zh, this message translates to:
  /// **'本地分类库'**
  String get ui593a76ae;

  /// Flule34 UI: 本地分类库无需登录；登录后还可查看网站收藏、历史和订阅。
  ///
  /// In zh, this message translates to:
  /// **'本地分类库无需登录；登录后还可查看网站收藏、历史和订阅。'**
  String get ui7afe5844;

  /// Flule34 UI: 本地库
  ///
  /// In zh, this message translates to:
  /// **'本地库'**
  String get ui0760582c;

  /// Flule34 UI: 本地诊断日志
  ///
  /// In zh, this message translates to:
  /// **'本地诊断日志'**
  String get ui5af2b9c7;

  /// Flule34 UI: 本机下载
  ///
  /// In zh, this message translates to:
  /// **'本机下载'**
  String get ui609a0e8a;

  /// Flule34 UI: 本机下载记录
  ///
  /// In zh, this message translates to:
  /// **'本机下载记录'**
  String get ui010aee81;

  /// Flule34 UI: 来源
  ///
  /// In zh, this message translates to:
  /// **'来源'**
  String get ui21a44385;

  /// Flule34 UI: 构建时间
  ///
  /// In zh, this message translates to:
  /// **'构建时间'**
  String get ui458ff22a;

  /// Flule34 UI: 构建模式
  ///
  /// In zh, this message translates to:
  /// **'构建模式'**
  String get ui06231f4e;

  /// Flule34 UI: 查找艺术家页面
  ///
  /// In zh, this message translates to:
  /// **'查找艺术家页面'**
  String get ui3a3a5f44;

  /// Flule34 UI: 查看 Flule34 与第三方 Flutter 依赖许可
  ///
  /// In zh, this message translates to:
  /// **'查看 Flule34 与第三方 Flutter 依赖许可'**
  String get ui32e834c8;

  /// Flule34 UI: 查看公开资料、上传内容和公开收藏
  ///
  /// In zh, this message translates to:
  /// **'查看公开资料、上传内容和公开收藏'**
  String get ui3c5ed424;

  /// Flule34 UI: 查看并复制不含凭据的运行环境摘要
  ///
  /// In zh, this message translates to:
  /// **'查看并复制不含凭据的运行环境摘要'**
  String get ui682b70e0;

  /// Flule34 UI: 查看诊断信息
  ///
  /// In zh, this message translates to:
  /// **'查看诊断信息'**
  String get ui37042e79;

  /// Flule34 UI: 标签
  ///
  /// In zh, this message translates to:
  /// **'标签'**
  String get ui3d8dc836;

  /// Flule34 UI: 标题
  ///
  /// In zh, this message translates to:
  /// **'标题'**
  String get ui669643c5;

  /// Flule34 UI: 标题、分类和标签可以分别选择显示原文、译文或双语。
  ///
  /// In zh, this message translates to:
  /// **'标题、分类和标签可以分别选择显示原文、译文或双语。'**
  String get ui04e99c7b;

  /// Flule34 UI: 检查更新
  ///
  /// In zh, this message translates to:
  /// **'检查更新'**
  String get ui308c78ab;

  /// Flule34 UI: 检查更新失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'检查更新失败：{p0}'**
  String ui5822474f(String p0);

  /// Flule34 UI: 检查更新超时，请稍后重试。
  ///
  /// In zh, this message translates to:
  /// **'检查更新超时，请稍后重试。'**
  String get ui3535d913;

  /// Flule34 UI: 模型列表拉取失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'模型列表拉取失败：{p0}'**
  String ui35ec3fa1(String p0);

  /// Flule34 UI: 模型名
  ///
  /// In zh, this message translates to:
  /// **'模型名'**
  String get ui703ce28e;

  /// Flule34 UI: 模糊视频封面
  ///
  /// In zh, this message translates to:
  /// **'模糊视频封面'**
  String get ui1375925f;

  /// Flule34 UI: 正在下载
  ///
  /// In zh, this message translates to:
  /// **'正在下载'**
  String get ui43f69efd;

  /// Flule34 UI: 正在下载 · {p0}
  ///
  /// In zh, this message translates to:
  /// **'正在下载 · {p0}'**
  String ui210fbca4(String p0);

  /// Flule34 UI: 正在刷新视频地址…
  ///
  /// In zh, this message translates to:
  /// **'正在刷新视频地址…'**
  String get ui34d9a170;

  /// Flule34 UI: 正在处理
  ///
  /// In zh, this message translates to:
  /// **'正在处理'**
  String get ui57036f5e;

  /// Flule34 UI: 正在播放媒体
  ///
  /// In zh, this message translates to:
  /// **'正在播放媒体'**
  String get ui1e85b6dc;

  /// Flule34 UI: 正在整理关注内容 {p0}/{p1}
  ///
  /// In zh, this message translates to:
  /// **'正在整理关注内容 {p0}/{p1}'**
  String ui01c66e0e(String p0, String p1);

  /// Flule34 UI: 正在读取全部视频…
  ///
  /// In zh, this message translates to:
  /// **'正在读取全部视频…'**
  String get ui37674019;

  /// Flule34 UI: 正在读取可用清晰度…
  ///
  /// In zh, this message translates to:
  /// **'正在读取可用清晰度…'**
  String get ui5323d64f;

  /// Flule34 UI: 正在读取收藏状态
  ///
  /// In zh, this message translates to:
  /// **'正在读取收藏状态'**
  String get ui334203a0;

  /// Flule34 UI: 正在读取日志信息…
  ///
  /// In zh, this message translates to:
  /// **'正在读取日志信息…'**
  String get ui0c3a23f3;

  /// Flule34 UI: 正在读取最近更新…
  ///
  /// In zh, this message translates to:
  /// **'正在读取最近更新…'**
  String get ui6b2b15cb;

  /// Flule34 UI: 正在读取最近更新（{p0}/{p1}）
  ///
  /// In zh, this message translates to:
  /// **'正在读取最近更新（{p0}/{p1}）'**
  String ui40cc44ec(String p0, String p1);

  /// Flule34 UI: 正在读取版本…
  ///
  /// In zh, this message translates to:
  /// **'正在读取版本…'**
  String get ui3016a852;

  /// Flule34 UI: 正在连接
  ///
  /// In zh, this message translates to:
  /// **'正在连接'**
  String get ui3de0c840;

  /// Flule34 UI: 此构建未配置 GitHub Releases 更新源。
  ///
  /// In zh, this message translates to:
  /// **'此构建未配置 GitHub Releases 更新源。'**
  String get ui108cc700;

  /// Flule34 UI: 此视频未提供可直接播放的 MP4 源。
  ///
  /// In zh, this message translates to:
  /// **'此视频未提供可直接播放的 MP4 源。'**
  String get ui3a0a0c97;

  /// Flule34 UI: 此视频没有可下载的 MP4 源。
  ///
  /// In zh, this message translates to:
  /// **'此视频没有可下载的 MP4 源。'**
  String get ui02c5ad74;

  /// Flule34 UI: 此视频源仍不可用，请重试刷新视频地址。
  ///
  /// In zh, this message translates to:
  /// **'此视频源仍不可用，请重试刷新视频地址。'**
  String get ui7cb7a0c5;

  /// Flule34 UI: 每次加载一批随机视频
  ///
  /// In zh, this message translates to:
  /// **'每次加载一批随机视频'**
  String get ui62dcc4bc;

  /// Flule34 UI: 每次询问
  ///
  /// In zh, this message translates to:
  /// **'每次询问'**
  String get ui51c846f1;

  /// Flule34 UI: 没有保存完成文件的位置。
  ///
  /// In zh, this message translates to:
  /// **'没有保存完成文件的位置。'**
  String get ui68fbffba;

  /// Flule34 UI: 没有匹配的已加载内容。
  ///
  /// In zh, this message translates to:
  /// **'没有匹配的已加载内容。'**
  String get ui13ed4ac5;

  /// Flule34 UI: 没有可导出的日志。
  ///
  ///
  /// In zh, this message translates to:
  /// **'没有可导出的日志。\n'**
  String get ui5198af87;

  /// Flule34 UI: 没有找到与“{p0}”匹配的{p1}。
  ///
  /// In zh, this message translates to:
  /// **'没有找到与“{p0}”匹配的{p1}。'**
  String ui61fe8d4a(String p0, String p1);

  /// Flule34 UI: 没有找到匹配的{p0}。
  ///
  /// In zh, this message translates to:
  /// **'没有找到匹配的{p0}。'**
  String ui02a64c6e(String p0);

  /// Flule34 UI: 没有找到同时满足这些条件的视频。
  ///
  /// In zh, this message translates to:
  /// **'没有找到同时满足这些条件的视频。'**
  String get ui6143fb85;

  /// Flule34 UI: 没有找到对应的本地标签译文或已学习标题译文。
  ///
  /// In zh, this message translates to:
  /// **'没有找到对应的本地标签译文或已学习标题译文。'**
  String get ui2aa03638;

  /// Flule34 UI: 没有找到相关{p0}。
  ///
  /// In zh, this message translates to:
  /// **'没有找到相关{p0}。'**
  String ui394bbe87(String p0);

  /// Flule34 UI: 没有找到符合条件的视频。
  ///
  /// In zh, this message translates to:
  /// **'没有找到符合条件的视频。'**
  String get ui335a4697;

  /// Flule34 UI: 没有找到视频。
  ///
  /// In zh, this message translates to:
  /// **'没有找到视频。'**
  String get ui3c55278f;

  /// Flule34 UI: 没有符合搜索和筛选条件的视频。
  ///
  /// In zh, this message translates to:
  /// **'没有符合搜索和筛选条件的视频。'**
  String get ui2855d008;

  /// Flule34 UI: 没有符合条件的下载记录。
  ///
  /// In zh, this message translates to:
  /// **'没有符合条件的下载记录。'**
  String get ui1cbeb77a;

  /// Flule34 UI: 没有符合条件的播放列表。
  ///
  /// In zh, this message translates to:
  /// **'没有符合条件的播放列表。'**
  String get ui3f6214e2;

  /// Flule34 UI: 没有符合条件的本地库。
  ///
  /// In zh, this message translates to:
  /// **'没有符合条件的本地库。'**
  String get ui5bcb2c9b;

  /// Flule34 UI: 没有符合条件的订阅。
  ///
  /// In zh, this message translates to:
  /// **'没有符合条件的订阅。'**
  String get ui3288b748;

  /// Flule34 UI: 没有符合条件的译文。
  ///
  /// In zh, this message translates to:
  /// **'没有符合条件的译文。'**
  String get ui1408d9d3;

  /// Flule34 UI: 注册账号
  ///
  /// In zh, this message translates to:
  /// **'注册账号'**
  String get ui0e0207cc;

  /// Flule34 UI: 注册邮箱
  ///
  /// In zh, this message translates to:
  /// **'注册邮箱'**
  String get ui34dc8c2e;

  /// Flule34 UI: 浅色
  ///
  /// In zh, this message translates to:
  /// **'浅色'**
  String get ui4782703e;

  /// Flule34 UI: 测试连接
  ///
  /// In zh, this message translates to:
  /// **'测试连接'**
  String get ui06cf3f13;

  /// Flule34 UI: 浏览站点内容分类
  ///
  /// In zh, this message translates to:
  /// **'浏览站点内容分类'**
  String get ui2bce8045;

  /// Flule34 UI: 浏览站点评分最高的视频
  ///
  /// In zh, this message translates to:
  /// **'浏览站点评分最高的视频'**
  String get ui1bdcacb9;

  /// Flule34 UI: 深色
  ///
  /// In zh, this message translates to:
  /// **'深色'**
  String get ui4e94fd7c;

  /// Flule34 UI: 添加
  ///
  /// In zh, this message translates to:
  /// **'添加'**
  String get ui68aa72b8;

  /// Flule34 UI: 清晰度
  ///
  /// In zh, this message translates to:
  /// **'清晰度'**
  String get ui28b4fe80;

  /// Flule34 UI: 清空
  ///
  /// In zh, this message translates to:
  /// **'清空'**
  String get ui1226aec8;

  /// Flule34 UI: 清空搜索历史？
  ///
  /// In zh, this message translates to:
  /// **'清空搜索历史？'**
  String get ui66d1872a;

  /// Flule34 UI: 清除
  ///
  /// In zh, this message translates to:
  /// **'清除'**
  String get ui3c5a0f54;

  /// Flule34 UI: 清除图片缓存
  ///
  /// In zh, this message translates to:
  /// **'清除图片缓存'**
  String get ui1e1dc2c5;

  /// Flule34 UI: 清除图片缓存失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'清除图片缓存失败：{p0}'**
  String ui198292d1(String p0);

  /// Flule34 UI: 清除应用日志？
  ///
  /// In zh, this message translates to:
  /// **'清除应用日志？'**
  String get ui2b78b9a7;

  /// Flule34 UI: 清除当前账号搜索历史
  ///
  /// In zh, this message translates to:
  /// **'清除当前账号搜索历史'**
  String get ui62aa01c1;

  /// Flule34 UI: 清除搜索
  ///
  /// In zh, this message translates to:
  /// **'清除搜索'**
  String get ui04093a21;

  /// Flule34 UI: 清除搜索历史失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'清除搜索历史失败：{p0}'**
  String ui21987264(String p0);

  /// Flule34 UI: 清除搜索历史？
  ///
  /// In zh, this message translates to:
  /// **'清除搜索历史？'**
  String get ui03f9bc1e;

  /// Flule34 UI: 清除播放进度失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'清除播放进度失败：{p0}'**
  String ui0e4abc92(String p0);

  /// Flule34 UI: 清除日志
  ///
  /// In zh, this message translates to:
  /// **'清除日志'**
  String get ui2b43d71b;

  /// Flule34 UI: 清除日志失败，请稍后重试。
  ///
  /// In zh, this message translates to:
  /// **'清除日志失败，请稍后重试。'**
  String get ui1f517bea;

  /// Flule34 UI: 清除条件
  ///
  /// In zh, this message translates to:
  /// **'清除条件'**
  String get ui47882249;

  /// Flule34 UI: 点击返回应用
  ///
  /// In zh, this message translates to:
  /// **'点击返回应用'**
  String get ui21697b99;

  /// Flule34 UI: 点赞率 ≥ {p0}%
  ///
  /// In zh, this message translates to:
  /// **'点赞率 ≥ {p0}%'**
  String ui26b5101f(String p0);

  /// Flule34 UI: 点赞率必须配合投票数判断，避免少量投票造成虚高。
  ///
  /// In zh, this message translates to:
  /// **'点赞率必须配合投票数判断，避免少量投票造成虚高。'**
  String get ui1894e352;

  /// Flule34 UI: 热门
  ///
  /// In zh, this message translates to:
  /// **'热门'**
  String get ui71e94df2;

  /// Flule34 UI: 热门标签
  ///
  /// In zh, this message translates to:
  /// **'热门标签'**
  String get ui41d23f81;

  /// Flule34 UI: 热门标签暂时不可用。
  ///
  /// In zh, this message translates to:
  /// **'热门标签暂时不可用。'**
  String get ui0e7f13ac;

  /// Flule34 UI: 热门视频
  ///
  /// In zh, this message translates to:
  /// **'热门视频'**
  String get ui795ab7fb;

  /// Flule34 UI: 热门视频、高评分视频和艺术家排行
  ///
  /// In zh, this message translates to:
  /// **'热门视频、高评分视频和艺术家排行'**
  String get ui5137980d;

  /// Flule34 UI: 版本 {p0}+{p1}
  ///
  /// In zh, this message translates to:
  /// **'版本 {p0}+{p1}'**
  String ui326c0193(String p0, String p1);

  /// Flule34 UI: 版本：{p0}
  ///
  /// In zh, this message translates to:
  /// **'版本：{p0}'**
  String ui3d81628e(String p0);

  /// Flule34 UI: 生成包含诊断信息和最近日志的文本文件。
  ///
  /// In zh, this message translates to:
  /// **'生成包含诊断信息和最近日志的文本文件。'**
  String get ui4627f6e6;

  /// Flule34 UI: 用户
  ///
  /// In zh, this message translates to:
  /// **'用户'**
  String get ui1be4cbb9;

  /// Flule34 UI: 用户 ID：{p0}
  ///
  /// In zh, this message translates to:
  /// **'用户 ID：{p0}'**
  String ui2ff2035d(String p0);

  /// Flule34 UI: 用户译文 {p0} 条。
  ///
  ///
  ///
  /// In zh, this message translates to:
  /// **'用户译文 {p0} 条。\n\n'**
  String ui07df625b(String p0);

  /// Flule34 UI: 由网站验证身份并处理邮箱变更
  ///
  /// In zh, this message translates to:
  /// **'由网站验证身份并处理邮箱变更'**
  String get ui02ac0fa7;

  /// Flule34 UI: 由网站验证身份并更新账号密码
  ///
  /// In zh, this message translates to:
  /// **'由网站验证身份并更新账号密码'**
  String get ui766b8c5d;

  /// Flule34 UI: 界面语言
  ///
  /// In zh, this message translates to:
  /// **'界面语言'**
  String get ui6f51d88d;

  /// Flule34 UI: 留空表示保留原密钥
  ///
  /// In zh, this message translates to:
  /// **'留空表示保留原密钥'**
  String get ui673b9a23;

  /// Flule34 UI: 登录
  ///
  /// In zh, this message translates to:
  /// **'登录'**
  String get ui3ad2af27;

  /// Flule34 UI: 登录后同步网站收藏、历史记录和订阅。
  ///
  /// In zh, this message translates to:
  /// **'登录后同步网站收藏、历史记录和订阅。'**
  String get ui6ddcc3eb;

  /// Flule34 UI: 登录后查看关注内容
  ///
  /// In zh, this message translates to:
  /// **'登录后查看关注内容'**
  String get ui03ac75d2;

  /// Flule34 UI: 登录后，搜索历史会按账号安全保存。
  ///
  /// In zh, this message translates to:
  /// **'登录后，搜索历史会按账号安全保存。'**
  String get ui4bd42f4c;

  /// Flule34 UI: 目标语言
  ///
  /// In zh, this message translates to:
  /// **'目标语言'**
  String get ui257d2512;

  /// Flule34 UI: 相关度
  ///
  /// In zh, this message translates to:
  /// **'相关度'**
  String get ui564ade2f;

  /// Flule34 UI: 相关视频
  ///
  /// In zh, this message translates to:
  /// **'相关视频'**
  String get ui5e5057d9;

  /// Flule34 UI: 确定
  ///
  /// In zh, this message translates to:
  /// **'确定'**
  String get ui271e4b44;

  /// Flule34 UI: 确定取消订阅“{p0}”吗？
  ///
  /// In zh, this message translates to:
  /// **'确定取消订阅“{p0}”吗？'**
  String ui5731dc83(String p0);

  /// Flule34 UI: 确认删除
  ///
  /// In zh, this message translates to:
  /// **'确认删除'**
  String get ui10bfd59a;

  /// Flule34 UI: 确认批量删除？
  ///
  /// In zh, this message translates to:
  /// **'确认批量删除？'**
  String get ui23a1a099;

  /// Flule34 UI: 票
  ///
  /// In zh, this message translates to:
  /// **'票'**
  String get ui22d867a3;

  /// Flule34 UI: 票数最多
  ///
  /// In zh, this message translates to:
  /// **'票数最多'**
  String get ui3e2a2939;

  /// Flule34 UI: 移出此库
  ///
  /// In zh, this message translates to:
  /// **'移出此库'**
  String get ui07f3e573;

  /// Flule34 UI: 移出此播放列表
  ///
  /// In zh, this message translates to:
  /// **'移出此播放列表'**
  String get ui332d29c7;

  /// Flule34 UI: 移除失效记录
  ///
  /// In zh, this message translates to:
  /// **'移除失效记录'**
  String get ui3890123e;

  /// Flule34 UI: 移除失效记录？
  ///
  /// In zh, this message translates to:
  /// **'移除失效记录？'**
  String get ui43f4c9b6;

  /// Flule34 UI: 稳定版
  ///
  /// In zh, this message translates to:
  /// **'稳定版'**
  String get ui3250d80e;

  /// Flule34 UI: 站内消息
  ///
  /// In zh, this message translates to:
  /// **'站内消息'**
  String get ui68bc4e82;

  /// Flule34 UI: 等待下载
  ///
  /// In zh, this message translates to:
  /// **'等待下载'**
  String get ui2ced8087;

  /// Flule34 UI: 等待重试
  ///
  /// In zh, this message translates to:
  /// **'等待重试'**
  String get ui106c1db7;

  /// Flule34 UI: 筛选
  ///
  /// In zh, this message translates to:
  /// **'筛选'**
  String get ui373ece32;

  /// Flule34 UI: 筛选与排序
  ///
  /// In zh, this message translates to:
  /// **'筛选与排序'**
  String get ui65b9a0f6;

  /// Flule34 UI: 筛选仅覆盖已加载内容，继续下滑可加载更多
  ///
  /// In zh, this message translates to:
  /// **'筛选仅覆盖已加载内容，继续下滑可加载更多'**
  String get ui0ea0c5c7;

  /// Flule34 UI: 筛选已加载的{p0}
  ///
  /// In zh, this message translates to:
  /// **'筛选已加载的{p0}'**
  String ui354b30cc(String p0);

  /// Flule34 UI: 筛选播放列表
  ///
  /// In zh, this message translates to:
  /// **'筛选播放列表'**
  String get ui269190a8;

  /// Flule34 UI: 筛选此库
  ///
  /// In zh, this message translates to:
  /// **'筛选此库'**
  String get ui72e0eba7;

  /// Flule34 UI: 筛选视频
  ///
  /// In zh, this message translates to:
  /// **'筛选视频'**
  String get ui2fe9e03b;

  /// Flule34 UI: 简介
  ///
  /// In zh, this message translates to:
  /// **'简介'**
  String get ui78a24072;

  /// Flule34 UI: 简体中文
  ///
  /// In zh, this message translates to:
  /// **'简体中文'**
  String get ui36e4a35c;

  /// Flule34 UI: 类型
  ///
  /// In zh, this message translates to:
  /// **'类型'**
  String get ui7aa38d36;

  /// Flule34 UI: 精选库 {p0} 包含重复视频。
  ///
  /// In zh, this message translates to:
  /// **'精选库 {p0} 包含重复视频。'**
  String ui0dbe3ac7(String p0);

  /// Flule34 UI: 精选库条目格式无效。
  ///
  /// In zh, this message translates to:
  /// **'精选库条目格式无效。'**
  String get ui3ae9eef9;

  /// Flule34 UI: 精选库条目缺少必要字段。
  ///
  /// In zh, this message translates to:
  /// **'精选库条目缺少必要字段。'**
  String get ui6d95458c;

  /// Flule34 UI: 精选库清单包含重复标识。
  ///
  /// In zh, this message translates to:
  /// **'精选库清单包含重复标识。'**
  String get ui082a7d52;

  /// Flule34 UI: 精选库清单格式无效。
  ///
  /// In zh, this message translates to:
  /// **'精选库清单格式无效。'**
  String get ui05f173f7;

  /// Flule34 UI: 精选库清单缺少版本或库列表。
  ///
  /// In zh, this message translates to:
  /// **'精选库清单缺少版本或库列表。'**
  String get ui48c2347b;

  /// Flule34 UI: 精选视频条目格式无效。
  ///
  /// In zh, this message translates to:
  /// **'精选视频条目格式无效。'**
  String get ui45724236;

  /// Flule34 UI: 精选视频条目缺少必要字段。
  ///
  /// In zh, this message translates to:
  /// **'精选视频条目缺少必要字段。'**
  String get ui3c28fff7;

  /// Flule34 UI: 系统中断|网络连接中断|connection reset|socketexception|timed?\s*out|broken pipe
  ///
  /// In zh, this message translates to:
  /// **'系统中断|网络连接中断|connection reset|socketexception|timed?\\s*out|broken pipe'**
  String get ui058d6015;

  /// Flule34 UI: 系统未授予公共下载目录写入权限。
  ///
  /// In zh, this message translates to:
  /// **'系统未授予公共下载目录写入权限。'**
  String get ui05a078da;

  /// Flule34 UI: 系统未能将任务加入下载队列。
  ///
  /// In zh, this message translates to:
  /// **'系统未能将任务加入下载队列。'**
  String get ui21f76d12;

  /// Flule34 UI: 系统未能重新加入下载任务。
  ///
  /// In zh, this message translates to:
  /// **'系统未能重新加入下载任务。'**
  String get ui111afc5c;

  /// Flule34 UI: 继续
  ///
  /// In zh, this message translates to:
  /// **'继续'**
  String get ui5cb65115;

  /// Flule34 UI: 继续加载并查找
  ///
  /// In zh, this message translates to:
  /// **'继续加载并查找'**
  String get ui0487b957;

  /// Flule34 UI: 继续向下滚动
  ///
  /// In zh, this message translates to:
  /// **'继续向下滚动'**
  String get ui16709544;

  /// Flule34 UI: 继续向下滚动以加载更多
  ///
  /// In zh, this message translates to:
  /// **'继续向下滚动以加载更多'**
  String get ui75e19e47;

  /// Flule34 UI: 继续手动填写
  ///
  /// In zh, this message translates to:
  /// **'继续手动填写'**
  String get ui4a3ada55;

  /// Flule34 UI: 综合
  ///
  /// In zh, this message translates to:
  /// **'综合'**
  String get ui0e97bdd4;

  /// Flule34 UI: 编辑
  ///
  /// In zh, this message translates to:
  /// **'编辑'**
  String get ui49512531;

  /// Flule34 UI: 编辑播放列表
  ///
  /// In zh, this message translates to:
  /// **'编辑播放列表'**
  String get ui07922887;

  /// Flule34 UI: 编辑翻译服务
  ///
  /// In zh, this message translates to:
  /// **'编辑翻译服务'**
  String get ui1d6b067d;

  /// Flule34 UI: 编辑译文
  ///
  /// In zh, this message translates to:
  /// **'编辑译文'**
  String get ui0faaeb98;

  /// Flule34 UI: 编辑资料
  ///
  /// In zh, this message translates to:
  /// **'编辑资料'**
  String get ui7d44f8fd;

  /// Flule34 UI: 网站个人主页
  ///
  /// In zh, this message translates to:
  /// **'网站个人主页'**
  String get ui59c1fe85;

  /// Flule34 UI: 网站收藏、历史和订阅以登录账号为边界；本地分类库保存在设备上，与账号无关。
  ///
  /// In zh, this message translates to:
  /// **'网站收藏、历史和订阅以登录账号为边界；本地分类库保存在设备上，与账号无关。'**
  String get ui166970fa;

  /// Flule34 UI: 网站要求填写验证码，因此由系统浏览器完成提交
  ///
  /// In zh, this message translates to:
  /// **'网站要求填写验证码，因此由系统浏览器完成提交'**
  String get ui6d8a839a;

  /// Flule34 UI: 网站观看历史还是空的。
  ///
  /// In zh, this message translates to:
  /// **'网站观看历史还是空的。'**
  String get ui52d40a61;

  /// Flule34 UI: 网站退出请求失败，但本地登录状态已经清除。
  ///
  /// In zh, this message translates to:
  /// **'网站退出请求失败，但本地登录状态已经清除。'**
  String get ui49712caa;

  /// Flule34 UI: 网站顺序
  ///
  /// In zh, this message translates to:
  /// **'网站顺序'**
  String get ui22be6add;

  /// Flule34 UI: 网络播放策略
  ///
  /// In zh, this message translates to:
  /// **'网络播放策略'**
  String get ui5c5b8e6e;

  /// Flule34 UI: 网络连接中断，请检查网络后重试。
  ///
  /// In zh, this message translates to:
  /// **'网络连接中断，请检查网络后重试。'**
  String get ui5d909650;

  /// Flule34 UI: 翻译失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'翻译失败：{p0}'**
  String ui4c8d7732(String p0);

  /// Flule34 UI: 翻译库
  ///
  /// In zh, this message translates to:
  /// **'翻译库'**
  String get ui20251330;

  /// Flule34 UI: 翻译服务
  ///
  /// In zh, this message translates to:
  /// **'翻译服务'**
  String get ui0e144c39;

  /// Flule34 UI: 翻译目标语言
  ///
  /// In zh, this message translates to:
  /// **'翻译目标语言'**
  String get ui4e721b57;

  /// Flule34 UI: 翻译设置
  ///
  /// In zh, this message translates to:
  /// **'翻译设置'**
  String get ui7312260a;

  /// Flule34 UI: 自动
  ///
  /// In zh, this message translates to:
  /// **'自动'**
  String get ui42682f0b;

  /// Flule34 UI: 自动或手动翻译时，每次只发送当前标题、标签或分类。服务按当前顺序依次尝试，失败后自动使用下一项。建议优先使用 AI 翻译，结果通常更自然、准确。
  ///
  /// In zh, this message translates to:
  /// **'自动或手动翻译时，每次只发送当前标题、标签或分类。服务按当前顺序依次尝试，失败后自动使用下一项。建议优先使用 AI 翻译，结果通常更自然、准确。'**
  String get ui3a3ee33c;

  /// Flule34 UI: 自动翻译
  ///
  /// In zh, this message translates to:
  /// **'自动翻译'**
  String get ui4e37cc82;

  /// Flule34 UI: 艺术家
  ///
  /// In zh, this message translates to:
  /// **'艺术家'**
  String get ui1d2c54c2;

  /// Flule34 UI: 艺术家排行榜
  ///
  /// In zh, this message translates to:
  /// **'艺术家排行榜'**
  String get ui273d81af;

  /// Flule34 UI: 节省流量
  ///
  /// In zh, this message translates to:
  /// **'节省流量'**
  String get ui296bcd5e;

  /// Flule34 UI: 视频
  ///
  /// In zh, this message translates to:
  /// **'视频'**
  String get ui7f179fc8;

  /// Flule34 UI: 视频保存路径：Download/Flule34
  ///
  /// In zh, this message translates to:
  /// **'视频保存路径：Download/Flule34'**
  String get ui4fbae4c2;

  /// Flule34 UI: 视频地址刷新后仍不可用，请稍后重试。
  ///
  /// In zh, this message translates to:
  /// **'视频地址刷新后仍不可用，请稍后重试。'**
  String get ui276089b3;

  /// Flule34 UI: 视频地址已连续刷新多次仍无法播放，请稍后手动重试。
  ///
  /// In zh, this message translates to:
  /// **'视频地址已连续刷新多次仍无法播放，请稍后手动重试。'**
  String get ui538cdd02;

  /// Flule34 UI: 视频布局
  ///
  /// In zh, this message translates to:
  /// **'视频布局'**
  String get ui6ad9c53c;

  /// Flule34 UI: 视频操作
  ///
  /// In zh, this message translates to:
  /// **'视频操作'**
  String get ui37bdf9f3;

  /// Flule34 UI: 视频数量
  ///
  /// In zh, this message translates to:
  /// **'视频数量'**
  String get ui604372e8;

  /// Flule34 UI: 视频时长
  ///
  /// In zh, this message translates to:
  /// **'视频时长'**
  String get ui7b794d8a;

  /// Flule34 UI: 视频源不能为空
  ///
  /// In zh, this message translates to:
  /// **'视频源不能为空'**
  String get ui63929b8d;

  /// Flule34 UI: 视频直接写入所选公共目录；默认目录为 Downloads/Flule34，可从“我的 → 下载”右上角进入设置。
  ///
  /// In zh, this message translates to:
  /// **'视频直接写入所选公共目录；默认目录为 Downloads/Flule34，可从“我的 → 下载”右上角进入设置。'**
  String get ui6b6d2d3c;

  /// Flule34 UI: 视频详情
  ///
  /// In zh, this message translates to:
  /// **'视频详情'**
  String get ui3c64ae15;

  /// Flule34 UI: 视频预览
  ///
  /// In zh, this message translates to:
  /// **'视频预览'**
  String get ui6fbc2348;

  /// Flule34 UI: 解锁控件
  ///
  /// In zh, this message translates to:
  /// **'解锁控件'**
  String get ui7b8f2379;

  /// Flule34 UI: 订阅
  ///
  /// In zh, this message translates to:
  /// **'订阅'**
  String get ui6e7502fd;

  /// Flule34 UI: 订阅页布局
  ///
  /// In zh, this message translates to:
  /// **'订阅页布局'**
  String get ui4c54789e;

  /// Flule34 UI: 记忆播放进度
  ///
  /// In zh, this message translates to:
  /// **'记忆播放进度'**
  String get ui3c79fc19;

  /// Flule34 UI: 设为私密
  ///
  /// In zh, this message translates to:
  /// **'设为私密'**
  String get ui5ab2c3c2;

  /// Flule34 UI: 设备
  ///
  /// In zh, this message translates to:
  /// **'设备'**
  String get ui592e7edb;

  /// Flule34 UI: 评分最高
  ///
  /// In zh, this message translates to:
  /// **'评分最高'**
  String get ui11313487;

  /// Flule34 UI: 诊断信息
  ///
  /// In zh, this message translates to:
  /// **'诊断信息'**
  String get ui3ce65beb;

  /// Flule34 UI: 诊断信息已复制。
  ///
  /// In zh, this message translates to:
  /// **'诊断信息已复制。'**
  String get ui442a175d;

  /// Flule34 UI: 译文
  ///
  /// In zh, this message translates to:
  /// **'译文'**
  String get ui0a2256ac;

  /// Flule34 UI: 译文不能为空
  ///
  /// In zh, this message translates to:
  /// **'译文不能为空'**
  String get ui5e9e6941;

  /// Flule34 UI: 语言显示模式
  ///
  /// In zh, this message translates to:
  /// **'语言显示模式'**
  String get ui52575ad3;

  /// Flule34 UI: 请先填写有效基址。
  ///
  /// In zh, this message translates to:
  /// **'请先填写有效基址。'**
  String get ui7894fed1;

  /// Flule34 UI: 请完整填写名称、基址、模型和密钥。
  ///
  /// In zh, this message translates to:
  /// **'请完整填写名称、基址、模型和密钥。'**
  String get ui190ff633;

  /// Flule34 UI: 请至少输入 2 个字符。
  ///
  /// In zh, this message translates to:
  /// **'请至少输入 2 个字符。'**
  String get ui61ca1aa4;

  /// Flule34 UI: 请输入密码。
  ///
  /// In zh, this message translates to:
  /// **'请输入密码。'**
  String get ui61cb4e40;

  /// Flule34 UI: 请输入注册邮箱。
  ///
  /// In zh, this message translates to:
  /// **'请输入注册邮箱。'**
  String get ui196453a1;

  /// Flule34 UI: 请返回“我的”页面登录后查看账号信息。
  ///
  /// In zh, this message translates to:
  /// **'请返回“我的”页面登录后查看账号信息。'**
  String get ui77044f29;

  /// Flule34 UI: 账号与媒体库
  ///
  /// In zh, this message translates to:
  /// **'账号与媒体库'**
  String get ui6447b2e3;

  /// Flule34 UI: 账号与安全
  ///
  /// In zh, this message translates to:
  /// **'账号与安全'**
  String get ui730cbb68;

  /// Flule34 UI: 账号中还没有播放列表。
  ///
  /// In zh, this message translates to:
  /// **'账号中还没有播放列表。'**
  String get ui6527aff1;

  /// Flule34 UI: 质量条件
  ///
  /// In zh, this message translates to:
  /// **'质量条件'**
  String get ui4f0bb3b1;

  /// Flule34 UI: 资料加载失败，重试
  ///
  /// In zh, this message translates to:
  /// **'资料加载失败，重试'**
  String get ui5e2feb59;

  /// Flule34 UI: 跟随界面语言
  ///
  /// In zh, this message translates to:
  /// **'跟随界面语言'**
  String get ui5236b1c3;

  /// Flule34 UI: 跟随系统
  ///
  /// In zh, this message translates to:
  /// **'跟随系统'**
  String get ui1c47ee05;

  /// Flule34 UI: 跳过 {p0}，
  ///
  /// In zh, this message translates to:
  /// **'跳过 {p0}，'**
  String ui76da0fc0(String p0);

  /// Flule34 UI: 过去 1 周
  ///
  /// In zh, this message translates to:
  /// **'过去 1 周'**
  String get ui739c6fd6;

  /// Flule34 UI: 过去 1 年
  ///
  /// In zh, this message translates to:
  /// **'过去 1 年'**
  String get ui5fd87a82;

  /// Flule34 UI: 过去 1 月
  ///
  /// In zh, this message translates to:
  /// **'过去 1 月'**
  String get ui431df5d6;

  /// Flule34 UI: 过去 2 天
  ///
  /// In zh, this message translates to:
  /// **'过去 2 天'**
  String get ui759f4739;

  /// Flule34 UI: 过去 24 小时
  ///
  /// In zh, this message translates to:
  /// **'过去 24 小时'**
  String get ui7790bf0c;

  /// Flule34 UI: 过去 3 月
  ///
  /// In zh, this message translates to:
  /// **'过去 3 月'**
  String get ui0a322b08;

  /// Flule34 UI: 返回
  ///
  /// In zh, this message translates to:
  /// **'返回'**
  String get ui58a37252;

  /// Flule34 UI: 还没有下载任务。
  ///
  /// In zh, this message translates to:
  /// **'还没有下载任务。'**
  String get ui10524b4c;

  /// Flule34 UI: 还没有搜索记录。
  ///
  /// In zh, this message translates to:
  /// **'还没有搜索记录。'**
  String get ui6e7397b9;

  /// Flule34 UI: 还没有本地库
  ///
  /// In zh, this message translates to:
  /// **'还没有本地库'**
  String get ui71607183;

  /// Flule34 UI: 还没有订阅内容。
  ///
  /// In zh, this message translates to:
  /// **'还没有订阅内容。'**
  String get ui7a38235f;

  /// Flule34 UI: 这个上传者还没有公开视频。
  ///
  /// In zh, this message translates to:
  /// **'这个上传者还没有公开视频。'**
  String get ui2f767daa;

  /// Flule34 UI: 这个播放列表里还没有视频。
  ///
  /// In zh, this message translates to:
  /// **'这个播放列表里还没有视频。'**
  String get ui3d2b959e;

  /// Flule34 UI: 这个本地库里还没有视频。
  ///
  /// In zh, this message translates to:
  /// **'这个本地库里还没有视频。'**
  String get ui1543885f;

  /// Flule34 UI: 这个订阅目前没有可显示的视频。
  ///
  /// In zh, this message translates to:
  /// **'这个订阅目前没有可显示的视频。'**
  String get ui08dc5995;

  /// Flule34 UI: 这个集合里暂时没有视频。
  ///
  /// In zh, this message translates to:
  /// **'这个集合里暂时没有视频。'**
  String get ui0432dab5;

  /// Flule34 UI: 进入全屏时横屏
  ///
  /// In zh, this message translates to:
  /// **'进入全屏时横屏'**
  String get ui6c1512dd;

  /// Flule34 UI: 连接失败：{p0}
  ///
  /// In zh, this message translates to:
  /// **'连接失败：{p0}'**
  String ui340178b5(String p0);

  /// Flule34 UI: 退出
  ///
  /// In zh, this message translates to:
  /// **'退出'**
  String get ui15cf6bb2;

  /// Flule34 UI: 退出全屏
  ///
  /// In zh, this message translates to:
  /// **'退出全屏'**
  String get ui61f69587;

  /// Flule34 UI: 退出当前账号
  ///
  /// In zh, this message translates to:
  /// **'退出当前账号'**
  String get ui27d0dda9;

  /// Flule34 UI: 退出登录
  ///
  /// In zh, this message translates to:
  /// **'退出登录'**
  String get ui60423290;

  /// Flule34 UI: 退出登录？
  ///
  /// In zh, this message translates to:
  /// **'退出登录？'**
  String get ui0c4a5e14;

  /// Flule34 UI: 选择下载清晰度
  ///
  /// In zh, this message translates to:
  /// **'选择下载清晰度'**
  String get ui1d37ed9d;

  /// Flule34 UI: 选择当前结果
  ///
  /// In zh, this message translates to:
  /// **'选择当前结果'**
  String get ui38e27fe6;

  /// Flule34 UI: 选择本地库
  ///
  /// In zh, this message translates to:
  /// **'选择本地库'**
  String get ui63947462;

  /// Flule34 UI: 选择模型
  ///
  /// In zh, this message translates to:
  /// **'选择模型'**
  String get ui2bbcf0c4;

  /// Flule34 UI: 选择跟随系统或固定使用一种界面语言
  ///
  /// In zh, this message translates to:
  /// **'选择跟随系统或固定使用一种界面语言'**
  String get ui53e6ce38;

  /// Flule34 UI: 通过配置的 GitHub Releases 源检查
  ///
  /// In zh, this message translates to:
  /// **'通过配置的 GitHub Releases 源检查'**
  String get ui5b975d06;

  /// Flule34 UI: 邮箱（可选）
  ///
  /// In zh, this message translates to:
  /// **'邮箱（可选）'**
  String get ui359a4400;

  /// Flule34 UI: 部分自动补全暂时不可用。
  ///
  /// In zh, this message translates to:
  /// **'部分自动补全暂时不可用。'**
  String get ui273538ab;

  /// Flule34 UI: 重命名
  ///
  /// In zh, this message translates to:
  /// **'重命名'**
  String get ui37f64133;

  /// Flule34 UI: 重命名本地库
  ///
  /// In zh, this message translates to:
  /// **'重命名本地库'**
  String get ui6fd9a2aa;

  /// Flule34 UI: 重新下载
  ///
  /// In zh, this message translates to:
  /// **'重新下载'**
  String get ui68e799c1;

  /// Flule34 UI: 重新检查
  ///
  /// In zh, this message translates to:
  /// **'重新检查'**
  String get ui3161da01;

  /// Flule34 UI: 重置
  ///
  /// In zh, this message translates to:
  /// **'重置'**
  String get ui611079ce;

  /// Flule34 UI: 重试
  ///
  /// In zh, this message translates to:
  /// **'重试'**
  String get ui3e06d854;

  /// Flule34 UI: 重试刷新
  ///
  /// In zh, this message translates to:
  /// **'重试刷新'**
  String get ui2fc2172a;

  /// Flule34 UI: 重试加载下一页
  ///
  /// In zh, this message translates to:
  /// **'重试加载下一页'**
  String get ui1f5c932b;

  /// Flule34 UI: 锁定控件
  ///
  /// In zh, this message translates to:
  /// **'锁定控件'**
  String get ui4a255d3c;

  /// Flule34 UI: 长按视频封面预览
  ///
  /// In zh, this message translates to:
  /// **'长按视频封面预览'**
  String get ui4e1780ec;

  /// Flule34 UI: 随机
  ///
  /// In zh, this message translates to:
  /// **'随机'**
  String get ui06efd73d;

  /// Flule34 UI: 随机探索
  ///
  /// In zh, this message translates to:
  /// **'随机探索'**
  String get ui74a56f94;

  /// Flule34 UI: 隐私与数据
  ///
  /// In zh, this message translates to:
  /// **'隐私与数据'**
  String get ui5d3798d3;

  /// Flule34 UI: 隐私说明
  ///
  /// In zh, this message translates to:
  /// **'隐私说明'**
  String get ui249b111a;

  /// Flule34 UI: 隐私说明：日志已自动脱敏，发送前仍建议自行检查。
  ///
  /// In zh, this message translates to:
  /// **'隐私说明：日志已自动脱敏，发送前仍建议自行检查。'**
  String get ui1c5806b0;

  /// Flule34 UI: 隐藏密码
  ///
  /// In zh, this message translates to:
  /// **'隐藏密码'**
  String get ui4b4e6624;

  /// Flule34 UI: 需要通知权限才能可靠显示后台下载进度。
  ///
  /// In zh, this message translates to:
  /// **'需要通知权限才能可靠显示后台下载进度。'**
  String get ui25621c61;

  /// Flule34 UI: 音乐
  ///
  /// In zh, this message translates to:
  /// **'音乐'**
  String get ui2555aad7;

  /// Flule34 UI: 音量 {p0}%
  ///
  /// In zh, this message translates to:
  /// **'音量 {p0}%'**
  String ui0727f3bc(String p0);

  /// Flule34 UI: 顺序播放
  ///
  /// In zh, this message translates to:
  /// **'顺序播放'**
  String get ui7f532d14;

  /// Flule34 UI: 预发布版
  ///
  /// In zh, this message translates to:
  /// **'预发布版'**
  String get ui73db46a3;

  /// Flule34 UI: 频道
  ///
  /// In zh, this message translates to:
  /// **'频道'**
  String get ui17cde1d0;

  /// Flule34 UI: 首页
  ///
  /// In zh, this message translates to:
  /// **'首页'**
  String get ui4bb87ce1;

  /// Flule34 UI: 首页、搜索和媒体库的视频卡片会模糊显示封面。
  ///
  /// In zh, this message translates to:
  /// **'首页、搜索和媒体库的视频卡片会模糊显示封面。'**
  String get ui75c36c5d;

  /// Flule34 UI: 首页默认内容取向
  ///
  /// In zh, this message translates to:
  /// **'首页默认内容取向'**
  String get ui11750af9;

  /// Flule34 UI: 高评分
  ///
  /// In zh, this message translates to:
  /// **'高评分'**
  String get ui669768f7;

  /// Flule34 UI: 高评分视频
  ///
  /// In zh, this message translates to:
  /// **'高评分视频'**
  String get ui1773f316;

  /// Flule34 UI: 默认播放清晰度
  ///
  /// In zh, this message translates to:
  /// **'默认播放清晰度'**
  String get ui349affc5;

  /// Flule34 UI: 默认顺序
  ///
  /// In zh, this message translates to:
  /// **'默认顺序'**
  String get ui41526a4f;

  /// Flule34 UI: （API {p0}、用户 {p1}）；
  ///
  /// In zh, this message translates to:
  /// **'（API {p0}、用户 {p1}）；'**
  String ui5c240b03(String p0, String p1);

  /// Flule34 UI: （精选）
  ///
  /// In zh, this message translates to:
  /// **'（精选）'**
  String get ui2102bc09;
}

class _AppLocalizationsDelegate
    extends LocalizationsDelegate<AppLocalizations> {
  const _AppLocalizationsDelegate();

  @override
  Future<AppLocalizations> load(Locale locale) {
    return SynchronousFuture<AppLocalizations>(lookupAppLocalizations(locale));
  }

  @override
  bool isSupported(Locale locale) =>
      <String>['en', 'ja', 'ko', 'zh'].contains(locale.languageCode);

  @override
  bool shouldReload(_AppLocalizationsDelegate old) => false;
}

AppLocalizations lookupAppLocalizations(Locale locale) {
  // Lookup logic when only language code is specified.
  switch (locale.languageCode) {
    case 'en':
      return AppLocalizationsEn();
    case 'ja':
      return AppLocalizationsJa();
    case 'ko':
      return AppLocalizationsKo();
    case 'zh':
      return AppLocalizationsZh();
  }

  throw FlutterError(
    'AppLocalizations.delegate failed to load unsupported locale "$locale". This is likely '
    'an issue with the localizations generation tool. Please file an issue '
    'on GitHub with a reproducible sample app and the gen-l10n configuration '
    'that was used.',
  );
}
