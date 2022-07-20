screen language_select tag menu:

    add 'video_prefs_bg'
    vbox:
        pos (40, 40)
        anchor (0, 0)
        hbox xpos 20:
            text _('Language:')
        null height 20
        for lang in languages:
            hbox:
                textbutton lang[1] action sets_language(lang[0]) xminimum 200
                if lang[0] == persistent.language:
                    null width 20
                    text _('(current)')
        null height 20
        if persistent.log_untranslated:
            text _('persistent.log_untranslated is true; missing translations will be prefixed\nwith *** and will be logged to translation_debugging.log.')
        else:
            text _('persistent.log_untranslated is false; translation logging is disabled.')
    use navigation_plaque

init python:
    def get_language_entry(subdir):
        print "Debug: Considering loading",subdir
        try:
            f = file(os.path.join(config.searchpath[0],'translations',subdir,'name'),'rb')
            name = f.readline().decode('utf-8')
            if name.endswith('\012'):
                name = name[:-1]
            return (subdir,name)
        except Exception,e:
            print "Loading language failed.",e
            return None

    def load_language_list():
        try:
            files = os.listdir(os.path.join(config.searchpath[0],'translations'))
            files.sort()
        except Exception,e:
            print "Error loading language list",e
            files = ()
        ret = [(None,'English')]
        for subdir in files:
            lang = get_language_entry(subdir)
            if lang:
                ret.append(lang)
        return ret

    def set_language(lang,quiet=False):
        unroller.compacted_translations.clear()
        unroller.tagless_translations.clear()
        config.translations.clear()
        config.say_menu_text_filter = _strip_translation_tags
        if lang is None:
            persistent.language = lang
            if not quiet:
                renpy.restart_interaction()
            return
        try:
            lines = file(os.path.join(config.searchpath[0],'translations',lang,'strings')).readlines()
            i = 0
            if lines and lines[0].startswith(unichr(65279).encode('utf-8')):
                lines[0] = filedata[0][3:]
            
            orig = None
            while i<len(lines):
                line = lines[i].replace('\\n','\n')
                if line.endswith('\012'):
                    line = line[:-1]
                if line.endswith('\015'):
                    line = line[:-1]
                if not line.startswith('#'):
                    line = line.decode('utf-8')
                    if orig is not None:
                        if line.startswith('{tag='):
                            if persistent.log_untranslated:
                                log_translation_missing("Tag present in translation of "+orig+" to "+line)
                            line = line.split('}',1)[-1]
                        config.translations[orig] = line
                        
                        if '  ' in orig or orig.endswith(' '):
                            while '  ' in orig:
                                orig = orig.replace('  ',' ')
                            if orig.endswith(' '): 
                                orig = orig[:-1]
                            unroller.compacted_translations[orig] = line
                        if orig.startswith('{tag='):
                            unroller.tagless_translations[orig.split('}',1)[1]] = line
                        orig = None
                    else:
                        orig = line
                i += 1
            config.say_menu_text_filter = _
            persistent.language = lang
            remap_visible_keyboard('translations/'+persistent.language+'/keyboard')
            if not quiet:
                renpy.restart_interaction()
        except Exception,e:
            print "Error:",e
            persistent.language = None
            if not quiet:
                global last_exception
                last_exception = str(e)
                unroller.translation_exception = e
                renpy.call_in_new_context('set_language_failed')

    sets_language = renpy.curry(set_language)
    log_translation_missing_set = set()

    def log_translation_missing(s):
        try:
            print persistent.language,"missing:",s
        except:
            print "Debug: missing string"
        if s in log_translation_missing_set:
            return
        try:
            f = file("translation-debugging.log","ab")
            f.writelines((str(persistent.language),' missing: ',s,'\n'))
            f.close()
            log_translation_missing_set.add(s)
        except Exception,e:
            print "Error logging missing string.",e

    def _(s):
        if s.startswith("{NOTRANS}"):
            
            return s[9:]
        if s in config.translations:
            
            ret = config.translations[s]
            if '{tag' in ret:
                ret = ret.replace('{tag','(tag')
                if persistent.log_untranslated:
                    log_translation_missing('*** Error: tag in translation for '+ret)
                    return '*** Error: tag in translation for '+ret
            return ret
        
        if s.startswith("{tag="):
            s2 = s.split('}',1)[-1]
            if s2 in config.translations:
                
                
                return config.translations[s2]
        
        
        
        if s in unroller.compacted_translations:
            return unroller.compacted_translations[s]
        
        if s.startswith('{tag='):
            s2 = s.split('}',1)[-1]
            if s2 in unroller.compacted_translations:
                return unroller.compacted_translations[s2]
            if s2 in unroller.tagless_translations:
                
                
                if persistent.log_untranslated and persistent.language:
                    log_translation_missing(s)
                    return '*~*'+unroller.tagless_translations[s2]
                return unroller.tagless_translations[s2]
        
        if persistent.log_untranslated and persistent.language:
            log_translation_missing(s)
            if s in unroller.tagless_translations:
                return '*~*'+unroller.tagless_translations[s]
            if s.startswith("{tag="):
                return '***'+s.replace('{','(')
            return '***'+s
        if s.startswith("{tag="):
            return s2
        return s

    def _strip_translation_tags(s):
        if s.startswith("{NOTRANS}"):
            return s[9:]
        if s.startswith("{tag="):
            return s.split('}',1)[-1]
        return s

    languages = load_language_list()
    import unroller
    set_language(persistent.language,quiet=True)


    readable_number_small_translations = dict()
    land_military_desc_translations = dict()
    barracks_report_translations = dict()
    readable_number_translations = dict()
    subgroup_translations = dict()
    activity_translations = dict()

    def translated_file_name(s):
        try:
            fn = 'translations/'+persistent.language+'/'+s
            renpy.file(fn).close()
            return fn
        except:
            return s

    renpy.display.text.text_tags['tag'] = False

label set_language_failed:
    menu:
        "An error occurred loading the new language:\n%(last_exception)s"
        "Ignore":
            pass
        "Traceback":
            $ raise
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
