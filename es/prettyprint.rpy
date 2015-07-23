init python:
    # Change these functions to apply your own language's rules as appropriate.

    def readable_number_small_translation(i):
        ret = ''
        if i!=int(i):
            rem = i-int(i)
            if i>=0 and i<=19 and rem>=.96:
                ret = 'almost '
                i = int(i+1)
            else:
                i = int(i)
        if i>=0 and i<=20:
            ret += ('no','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty')[int(i)]
        else:
            ret = str(i)
        if rem>=.88 and rem<.96:
            ret += ' and nine tenths'
        elif rem>=.73:
            ret += ' and three quarters'
        elif rem>=.6:
            ret += ' and over a half'
        elif rem>=.47:
            ret += ' and a half'
        elif rem>=.4:
            ret += ' and almost a half'
        elif rem>=.2:
            ret += ' and a quarter'
        elif rem>=.07:
            ret += ' and a tenth'
        elif rem>.03:
            ret = 'a shade over '+ret
        if ret.startswith('no and '):
            ret = ret[7:]
        return ret

    # and change 'raw' to the directory name the translation files are in.
    # If you don't want to use a function, comment it and the lines pertaining
    # to it out and the game will fall back to simple stringification for most
    # functions.  You will need to include barracks_report_translation,
    # however.

    readable_number_small_translations['raw'] = readable_number_small_translation
    def land_military_desc_translation(soldiers):
        if int(soldiers/1200.0):
            return readable_number_small(soldiers/1200.0)+' battalions'
        elif soldiers/1200.0<=.03:
            return 'a handful of soldiers'
        elif soldiers/1200.0<.07:
            return "about a platoon"
        return readable_number_small(soldiers/1200.0)+' of a battalion'
    land_military_desc_translations['raw'] = land_military_desc_translation

    def barracks_report_translation(amt):
        battalions = int(amt/1200)
        amt -= battalions*1200
        companies = 0
        platoons = 0
        if amt>0:
            companies = int(amt/300)
            amt -= companies*300
        if amt>0:
            platoons = max(int(amt/100),1)
        ret = ''
        if battalions:
            ret = readable_number(battalions)+' '
            if battalions>1:
                ret += 'battalions'
            else:
                ret += 'battalion'
        if companies:
            if battalions and platoons:
                ret += ', '
            else:
                ret += ' and '
            ret += readable_number(companies)
            if companies>1:
                ret += ' companies'
            else:
                ret += ' company'
        if platoons:
            if companies and battalions:
                ret += ', and '
            elif companies or battalions:
                ret += ' and '
            ret += readable_number(platoons)+' '
            if platoons>1:
                ret += 'platoons'
            else:
                ret += 'platoon'
        return ret

    barracks_report_translations['raw'] = barracks_report_translation

    def readable_number_translation(i):
        if i!=int(i):
            i = int(i)
        if not i:
            return 'no'
        ret = ''
        if i>1000:
            ret = readable_number(i/1000)+' thousand'
            i = i % 1000
        if i>=100:
            if ret:
                ret += ', '
            ret += num_words[i/100]+' hundred'
        i = i%100
        if i:
            if ret:
                ret += ' and '
            if i<len(num_words):
                return ret+num_words[i]
            ret += tens[i/10]
            if i/10>=1 and i%10:
                ret += '-'
            i %= 10
            if i:
                ret += num_words[i]
        return ret
    readable_number_translations['raw'] = readable_number_translation
