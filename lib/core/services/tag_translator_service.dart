import 'dart:convert';
import 'package:flutter/services.dart' show rootBundle;

class TagTranslatorService {
  final Map<String, String> _dictionary = {};
  bool _initialized = false;

  Future<void> init() async {
    if (_initialized) return;

    try {
      final csvString = await rootBundle.loadString('assets/tags/rule34video_tags_zh.csv');
      final lines = const LineSplitter().convert(csvString);
      
      bool isFirstLine = true;
      for (final line in lines) {
        if (line.isEmpty) continue;
        if (isFirstLine && line.startsWith('ID,')) {
          isFirstLine = false;
          continue;
        }
        
        final parts = line.split(',');
        if (parts.length >= 3) {
          var name = parts[1].trim();
          var cnName = parts[2].trim();
          
          if (name.startsWith('"') && name.endsWith('"')) {
            name = name.substring(1, name.length - 1);
          }
          if (cnName.startsWith('"') && cnName.endsWith('"')) {
            cnName = cnName.substring(1, cnName.length - 1);
          }
          
          if (name.isNotEmpty && cnName.isNotEmpty && name.toLowerCase() != cnName.toLowerCase()) {
            _dictionary[name.toLowerCase()] = cnName;
            _dictionary[name.toLowerCase().replaceAll(' ', '_')] = cnName;
            _dictionary[name.toLowerCase().replaceAll('_', ' ')] = cnName;
          }
        }
      }
      _initialized = true;
    } catch (_) {
      // ignore
    }
  }

  void dispose() {
    _dictionary.clear();
  }

  String translate(String tag) {
    if (!_initialized || tag.trim().isEmpty) return tag;
    
    final normalized = tag.trim().toLowerCase();
    
    if (_dictionary.containsKey(normalized)) {
      final cnName = _dictionary[normalized]!;
      return '$tag ($cnName)';
    }

    return tag;
  }
}
