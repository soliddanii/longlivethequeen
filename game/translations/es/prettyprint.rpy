init python:
    # Change these functions to apply your own language's rules as appropriate.
    # Notice the u' for allow encode to utf-8 characters like í

    def readable_number_small_translation(i):
        ret = ''
        if i != int(i):
            rem = i-int(i)
            if i >= 0 and i <= 19 and rem >= .96:
                ret = 'casi '
                i = int(i+1)
            else:
                i = int(i)
        if i >= 0 and i <= 20:
            ret += ('cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once',
                    'doce', 'trece', 'catorce', 'quince', u'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve', 'veinte')[int(i)]
        else:
            ret = str(i)
        if rem >= .88 and rem < .96:
            ret += u' y nueve décimas'
        elif rem >= .73:
            ret += ' y tres cuartos'
        elif rem >= .6:
            ret += ' y mas de la mitad'
        elif rem >= .47:
            ret += ' y la mitad'
        elif rem >= .4:
            ret += ' y casi la mitad'
        elif rem >= .2:
            ret += ' y un cuarto'
        elif rem >= .07:
            ret += ' y un decimo'
        elif rem > .03:
            ret = 'un poco mas de '+ret
        if ret.startswith('cero y '):
            ret = ret[7:]
        return ret

    # and change 'raw' to the directory name the translation files are in.
    # If you don't want to use a function, comment it and the lines pertaining
    # to it out and the game will fall back to simple stringification for most
    # functions.  You will need to include barracks_report_translation,
    # however.

    readable_number_small_translations['es'] = readable_number_small_translation

    def land_military_desc_translation(soldiers):
        if int(soldiers/1200.0):
            return readable_number_small(soldiers/1200.0)+' batallones'
        elif soldiers/1200.0 <= .03:
            return u'un puñado de soldados'
        elif soldiers/1200.0 < .07:
            return u'un pelotón'
        return readable_number_small(soldiers/1200.0)+' de un batallon'
    land_military_desc_translations['es'] = land_military_desc_translation

    def barracks_report_translation(amt):
        battalions = int(amt/1200)
        amt -= battalions*1200
        companies = 0
        platoons = 0
        if amt > 0:
            companies = int(amt/300)
            amt -= companies*300
        if amt > 0:
            platoons = max(int(amt/100), 1)
        ret = ''
        if battalions:
            ret = readable_number(battalions)+' '
            if battalions > 1:
                ret += 'batallones'
            else:
                ret += u'batallón'
        if companies:
            if battalions and platoons:
                ret += ', '
            else:
                ret += ' y '
            ret += readable_number(companies)
            if companies > 1:
                ret += u' compañias'
            else:
                ret += u' compañia'
        if platoons:
            if companies and battalions:
                ret += ', y '
            elif companies or battalions:
                ret += ' y '
            ret += readable_number(platoons)+' '
            if platoons > 1:
                ret += 'pelotones'
            else:
                ret += u'pelotón'
        return ret

    barracks_report_translations['es'] = barracks_report_translation

    num_words = ['cero', 'un', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once',
                 'doce', 'trece', 'catorce', 'quince', u'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve', 'veinte']

    def readable_number_translation(i):
        if i != int(i):
            i = int(i)
        if not i:
            return 'no'
        ret = ''
        if i > 1000:
            ret = readable_number(i/1000)+' mil'
            i = i % 1000
        if i > 100:
            if ret:
                ret += ', '
            ret += num_words[i/100]+' cientos'
        i = i % 100
        if i == 100:
            if ret:
                ret += ', '
            ret += ' cien'
        i = i % 100
        if i:
            if ret:
                ret += ' y '
            if i < len(num_words):
                return ret+num_words[i]
            ret += tens[i/10]
            if i/10 >= 1 and i % 10:
                ret += '-'
            i %= 10
            if i:
                ret += num_words[i]
        return ret
    readable_number_translations['es'] = readable_number_translation

    # Change the dict for allow the translation of the values
    # %(subgroup)s and %(activity)s
    # eg: dict({'Military': 'Ciencias Militares', 'Weapons':'Armas'})

    def subgroup_translation():
        return dict({
            # Social
            'Royal Demeanor': 'Conducta',
            'Conversation': u'Conversación',
            'Expression': u'Expresión',
            # Physical
            'Agility': 'Agilidad',
            'Weapons': 'Armas',
            'Athletics': 'Atletismo',
            'Animal Handling': 'Cuidado Animal',
            # Intellectual
            'History': 'Historia',
            'Intrigue': 'Intriga',
            'Medicine': 'Medicina',
            'Economics': u'Economía',
            'Military': 'Ciencias Militares',
            # Mystical
            'Faith': 'Fe',
            'Lumen': 'Lumen'
        })

    subgroup_translations['es'] = subgroup_translation

    def activity_translation():
        return dict({
            # Royal Demeanor
            'Composure': 'Serenidad',
            'Elegance': 'Elegancia',
            'Presence': 'Presencia',
            # Conversation
            'Public Speaking': u'Hablar en Público',
            'Court Manners': 'Modales',
            'Flattery': u'Adulación',
            # Expression
            'Decoration': u'Decoración',
            'Instrument': 'Instrumento',
            'Voice': 'Voz',
            # History
            'Novan History': 'Historia de Nova',
            'Foreign Affairs': 'Historia Externa',
            'World History': 'Historia del Mundo',
            # Intrigue
            'Internal Affairs': 'Asuntos Internos',
            'Foreign Intelligence': 'Asuntos Externos',
            'Ciphering': 'Cifrado',
            # Medicine
            'Herbs': 'Hierbas',
            'Battlefield Medicine': 'Medicina de Batalla',
            'Poison': 'Veneno',
            # Economics
            'Accounting': 'Contabilidad',
            'Trade': 'Comercio',
            'Production': u'Producción',
            # Military
            'Strategy': 'Estrategia',
            'Naval Strategy': 'Estrategia Naval',
            'Logistics': u'Logística',
            # Agility
            'Dance': 'Baile',
            'Reflexes': 'Reflejos',
            'Flexibility': 'Flexibilidad',
            # Weapons
            'Swords': 'Espadas',
            'Archery': 'Tiro con arco',
            'Polearms': 'Alabardas',
            # Athletics
            'Running': 'Atletismo',
            'Climbing': 'Escalada',
            'Swimming': u'Natación',
            # Animal Handling
            'Horses': 'Caballos',
            'Dogs': 'Perros',
            'Falcons': 'Halcones',
            # Faith
            'Meditation': u'Meditación',
            'Divination': u'Adivinación',
            'Lore': 'Lore',
            # Lumen
            'Sense Magic': 'Percibir Magia',
            'Resist Magic': 'Resistir Magia',
            'Wield Magic': 'Usar Magia'
        })

    activity_translations['es'] = activity_translation
