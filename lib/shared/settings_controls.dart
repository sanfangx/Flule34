import 'package:flutter/material.dart';

import '../l10n/ui_localization.dart';

class SettingsField extends StatelessWidget {
  const SettingsField({
    super.key,
    required this.title,
    required this.child,
    this.description,
    this.padding = const EdgeInsets.only(bottom: 8),
  });

  final String title;
  final String? description;
  final Widget child;
  final EdgeInsetsGeometry padding;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: padding,
      child: DecoratedBox(
        decoration: BoxDecoration(
          color: Theme.of(context).colorScheme.surfaceContainerLow,
          borderRadius: BorderRadius.circular(8),
        ),
        child: Padding(
          padding: const EdgeInsets.all(14),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              AppText(title, style: Theme.of(context).textTheme.titleMedium),
              if (description != null) ...[
                const SizedBox(height: 4),
                AppText(
                  description!,
                  style: Theme.of(context).textTheme.bodySmall,
                ),
              ],
              const SizedBox(height: 10),
              child,
            ],
          ),
        ),
      ),
    );
  }
}

class SettingsSwitchField extends StatelessWidget {
  const SettingsSwitchField({
    super.key,
    required this.title,
    required this.value,
    required this.onChanged,
    this.description,
  });

  final String title;
  final String? description;
  final bool value;
  final ValueChanged<bool>? onChanged;

  @override
  Widget build(BuildContext context) {
    return SettingsField(
      title: title,
      description: description,
      child: Row(
        children: [
          AppText(value ? '已开启' : '已关闭'),
          const Spacer(),
          Switch(value: value, onChanged: onChanged),
        ],
      ),
    );
  }
}

class SettingsDropdownField<T> extends StatelessWidget {
  const SettingsDropdownField({
    super.key,
    required this.title,
    required this.value,
    required this.items,
    required this.onChanged,
    this.description,
  });

  final String title;
  final String? description;
  final T value;
  final List<DropdownMenuItem<T>> items;
  final ValueChanged<T?>? onChanged;

  @override
  Widget build(BuildContext context) {
    return SettingsField(
      title: title,
      description: description,
      child: DropdownButtonFormField<T>(
        key: ValueKey(value),
        initialValue: value,
        isExpanded: true,
        decoration: const InputDecoration(border: OutlineInputBorder()),
        items: items,
        onChanged: onChanged,
      ),
    );
  }
}
