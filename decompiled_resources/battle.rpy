label first_ixion_nonmagical_battle:












    call switchfade_fragile_calm
    "You receive a report on the outcome of the battle against the Ixionites."
    python:
        soldiers_lost = int((.86-(((strategy+(logistics*.2))*.01)*.36))*1200)
        add_army_size(-soldiers_lost) 
        flags['week10_battle_loss_soldiers'] = soldiers_lost
        anger = add_mood(anger,1)
    if flags['week10_battle_loss_soldiers']<=600:
        "You succeeded in driving them out of Maree, but it cost you half a battalion of soldiers and a great deal of materiel."
    elif flags['week10_battle_loss_soldiers']<700:
        "You succeeded in driving them out of Maree, but it cost you over half a battalion of soldiers and a great deal of materiel."
    elif flags['week10_battle_loss_soldiers']<900:
        "You succeeded in driving them out of Maree, but it cost you about three quarters of a battalion of soldiers and a great deal of materiel."
    else:
        "You succeeded in driving them out of Maree, but it cost you almost a full battalion of soldiers and a great deal of materiel."
    "You lost %(soldiers_lost)d soldiers."
    python:
        moodbubble('+1 Angry')
    elodie_angry "The Duke of Maree will be happy, but we could have done better!"


    return

init python:
    def pre_civil_war_military_strength():
        if 'army_size' in flags:
            return flags['army_size']
        ret = 12000 - flags.get('week10_battle_loss_soldiers',0)
        ret -= flags.get('week18_personal_guard',0)
        if flags.get('week20_sedna_response','')=='soldiers':
            ret -= 1200
        if flags.get('week24_lillah_action','')=='arrest':
            ret -= 400
        if flags.get('week25_lillah_action','')=='arrest':
            ret -= 400
        if flags.get('week15_first_printing','')=='army':
            ret += 500
        if 'week25_shanjia_omen_cost' in flags:
            ret += 1000
        if 'week27_sedna_reinforcements' in flags:
            ret -= 1200
        return ret

    def military_strength(mul=1.0):
        if 'army_size' in flags:
            return flags['army_size']*mul
        ret = pre_civil_war_military_strength()*mul
        if flags.get('week29_pardon',False):
            
            ret += 623
        if flags.get('week29_shanjia_pardon',False):
            
            ret += 879
        if 'civil_war_victory' in flags:
            ret -= rebel_loss_soldiers
            ret -= loyalist_loss_soldiers
        if flags.get('week31_omen','')=='dispatch east':
            ret -= 1200
        if flags.get('week32_prize','')=='employment':
            ret += 400
        if flags.get('week34_recruit',False):
            ret += int(flags['week34_recruit_cost']*.5)
        return ret












    def readable_number_small(i):
        if persistent.language is not None:
            if persistent.language in readable_number_small_translations:
                return readable_number_small_translations[persistent.language](i)
            if i==int(i):
                return str(int(i))
            return "%.02f"%i
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
    def land_military_desc(soldiers):
        if persistent.language is not None:
            if persistent.language in land_military_desc_translations:
                return land_military_desc_translations[persistent.language](soldiers)
            return str(int(soldiers))
        if int(soldiers/1200.0):
            return readable_number_small(soldiers/1200.0)+' battalions'
        elif soldiers/1200.0<=.03:
            return 'a handful of soldiers'
        elif soldiers/1200.0<.07:
            return "about a platoon"
        return readable_number_small(soldiers/1200.0)+' of a battalion'

    def naval_military_strength():
        ret = military_strength()
        if flags.get('week25_shanjia_action','')=='warships':
            ret += 3000
        if flags.get('week35_ixion_aid_success',False):
            ret += 2000
        return ret
    def shanjia_naval_battle_victory():
        bonus = .0
        if naval_strategy<=0:
            bonus = -.25 
        elif naval_strategy>=50:
            bonus = (naval_strategy-50)/1000.0 
            if flags['week34_fleet'] and climbing>=60:
                bonus += (naval_strategy/10000.) 
        if naval_strategy>=100:
            bonus += (strategy/2000.) 
        if logistics>=90:
            bonus += (logistics/2000.) 
        if not flags['week34_fleet']:
            bonus *= .5 
        elif wield_magic>=60:
            bonus += .05
            if flags['week34_fleet'] and climbing>=60:
                bonus += wield_magic/3333.  
        nova_power = naval_military_strength()
        nova_power += (nova_power*bonus)
        shanjia_power = shanjian_military_strength()
        return nova_power>=shanjia_power
    def shanjian_military_strength():
        if 'week35_big_magic' in flags:
            return 9000
        return 18000

    def add_army_size(amt):
        
        
        
        if 'army_size' not in flags:
            flags['army_size'] = military_strength()+amt
            return
        flags['army_size'] += amt

    def barracks_report(amt):
        if (persistent.language is not None) and persistent.language in barracks_report_translations:
            return barracks_report_translations[persistent.language](amt)
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

    def civil_war_in_progress():
        if 'week29_pardon' not in flags:
            return False
        if 'week30_war_resolution' in flags:
            return False
        if weeknum>=32:
            return False
        if flags.get('week30_surrender_marry','') == 'compromise' and not 'week30_surrender_compromise_failed':
            return False
        if 'week28_arisse_advisor' in flags:
            return False
        return True

label visit_barracks:
    python:
        switchfade('music/hunting (sozai12).ogg')
        if not civil_war_in_progress():
            barracks_fluff = barracks_report(flags['army_size'])
        else:
            barracks_fluff = barracks_report(int(flags['army_size']*loyalist_percent))
        crowded = add_mood(crowded,1)
        if weeknum>=35 and 'week35_shanjia_naval_victory' not in flags and not flags.get('week35_shanjia_defeat'):
            cheerfulness = add_mood(cheerfulness, -1)
            moodbubbles("+1 Depressed","+1 Pressured")
        elif willful>0:
            willful -= 1
            moodbubbles("-1 Willful",'+1 Pressured')
        elif willful<0:
            willful += 1
            moodbubbles("-1 Yielding",'+1 Pressured')
        else:
            moodbubble('+1 Pressured')
    if weeknum>=35 and 'week35_shanjia_naval_victory' not in flags and not flags.get('week35_shanjia_defeat'):
        "The barracks stand largely empty. What remains of your army is scattered."
        return
    if not civil_war_in_progress():
        "You are impressed by the discipline of the Novan troops, but the responsibility for their lives weighs heavily on your shoulders."
    else:
        "You are impressed by the discipline of the loyal Novan troops, but the responsibility for their lives weighs heavily on your shoulders."
    if weeknum>=35:
        return
    "There are approximately %(barracks_fluff)s under your direct command."
    if flags.get('week25_shanjia_action','')=='warships':
        if weeknum<32:
            "Progress on your new warships reportedly proceeds apace."
        elif weeknum<35:
            "Your newest ships of the line are undergoing final checkout."
    return


label week25_shanjia_info:
    if show_test('World History',world_history>=100):
        elodie_angry "(The Queen of Shanjia has been conquering her smaller neighbors recently.)"
    elif show_test('Foreign Affairs',foreign_affairs>=20,delay=.5):
        elodie_angry "(Shanjia has been growing larger in recent years.)"
    "Shanjia lies a great distance from Nova. You have few diplomatic ties and no known conflicts. There's no reason to assume that you would be their target."
    "Still, if they send a fleet across the ocean, Nova might be in danger. At the very least, shipping would be disrupted."
    if show_test('Trade',trade>=80,partial=trade>=40):
        elodie_angry "(And that would be a disaster to the Novan economy. We have to keep the shipping lanes clear.)"
    elif trade>=40:
        elodie_angry "(The western ocean is very important to Novan trade. That could cause problems.)"
    "It takes time to assemble worthy vessels, and you have advance warning. You could make your own preparations to defend your coast."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
