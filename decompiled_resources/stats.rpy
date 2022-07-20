init python:

    def apply_mood_bonuses():
        global faith_bonus
        global agility_bonus
        global royal_demeanor_bonus
        global weapons_bonus
        global military_bonus
        global intrigue_bonus
        global medicine_bonus
        global animal_handling_bonus
        global expression_bonus
        global athletics_bonus
        global conversation_bonus
        global lumen_bonus
        global economics_bonus
        global history_bonus
        if mood=='Afraid':
            faith_bonus += 1
            agility_bonus += 1
            royal_demeanor_bonus -= 1
            weapons_bonus -= 1
            military_bonus -= 1
            intrigue_bonus -= 1
        elif mood=='Angry':
            weapons_bonus += 1
            military_bonus += 1
            royal_demeanor_bonus -= 1
            medicine_bonus -= 1
            animal_handling_bonus -= 1
            expression_bonus -= 1
        elif mood=='Depressed':
            expression_bonus += 1
            animal_handling_bonus += 1
            royal_demeanor_bonus -= 1
            conversation_bonus -= 2
            athletics_bonus -= 1
        elif mood=='Cheerful':
            athletics_bonus += 1
            conversation_bonus += 1
            weapons_bonus -= 1
            military_bonus -= 2
            intrigue_bonus -= 1
        elif mood=='Yielding':
            history_bonus += 1
            royal_demeanor_bonus += 1
            faith_bonus += 1
            lumen_bonus -= 3
            weapons_bonus -= 3
        elif mood=='Willful':
            lumen_bonus += 1
            intrigue_bonus += 1
            military_bonus += 1
            royal_demeanor_bonus -= 2
            history_bonus -= 2
            economics_bonus -= 2
        elif mood=='Lonely':
            conversation_bonus += 1
            medicine_bonus += 1
            faith_bonus -= 1
            royal_demeanor_bonus -= 1
            intrigue_bonus -= 1
        elif mood=='Pressured':
            athletics_bonus += 1
            faith_bonus += 1
            conversation_bonus -= 1
            history_bonus -= 1
            economics_bonus -= 1
        elif mood=='Injured':
            agility_bonus -= 3
            weapons_bonus -= 3
            athletics_bonus -= 3
            animal_handling_bonus -= 3

    def update_bonuses():
        global royal_demeanor_bonus
        royal_demeanor_bonus = (composure_+elegance_+presence_)*.01
        global conversation_bonus
        conversation_bonus = (public_speaking_+court_manners_+flattery_)*.01
        global expression_bonus
        expression_bonus = (decoration_+instrument_+voice_skill_)*.01
        global social_bonus
        social_bonus = (royal_demeanor_bonus+conversation_bonus+expression_bonus)*.1
        
        global agility_bonus
        agility_bonus = (dance_+reflexes_+flexibility_)*.01
        global weapons_bonus
        weapons_bonus = (swords_+archery_+polearms_)*.01
        global athletics_bonus
        athletics_bonus = (running_+climbing_+swimming_)*.01
        global animal_handling_bonus
        animal_handling_bonus = (horses_+dogs_+falcons_)*.01
        global physical_bonus
        physical_bonus = (agility_bonus+weapons_bonus+athletics_bonus+animal_handling_bonus)*.1
        
        global history_bonus
        history_bonus = (novan_history_+foreign_affairs_+world_history_)*.01
        global intrigue_bonus
        intrigue_bonus = (internal_affairs_+foreign_intelligence_+ciphering_)*.01
        global medicine_bonus
        medicine_bonus = (herbs_+battlefield_medicine_+poison_)*.01
        global economics_bonus
        economics_bonus = (accounting_+trade_+production_)*.01
        global military_bonus
        military_bonus = (strategy_+naval_strategy_+logistics_)*.01
        global intellectual_bonus
        intellectual_bonus = (history_bonus+intrigue_bonus+medicine_bonus+economics_bonus+military_bonus)*.1
        
        global faith_bonus
        faith_bonus = (meditation_+divination_+lore_)*.01
        global lumen_bonus
        lumen_bonus = (sense_magic_+resist_magic_+wield_magic_)*.01
        global mystical_bonus
        mystical_bonus = (faith_bonus+lumen_bonus)*.1
        determine_mood()
        apply_mood_bonuses()

    stat_descs = {
        'Composure':'the ability to bear pain, fear, and surprise without flinching',
        'Elegance':'the ability to be beautiful and dignified under any circumstances',
        'Presence':'an aura of confidence and command',
        'Public Speaking': 'the ability to use words well under pressure',
        'Court Manners': 'proper etiquette for all situations',
        'Flattery':'the ability to tell someone what they want to hear',
        'Decoration':'drawing, painting, arranging flowers, dressing well',
        'Instrument':'skill with musical instruments such as the harp and flute',
        'Voice':'the skill of singing beautifully',
            'Novan History':'notable events and locations within this domain',
        'Foreign Affairs':'notable events and relationships between this domain and its neighbors',
        'World History':'long-term information about the world in general',
        'Internal Affairs':'what the nobles and other citizens are up to',
        'Foreign Intelligence':'what other countries are up to',
        'Ciphering':'learning to read and write secret information',
        'Herbs':'knowledge of helpful and harmful plants',
        'Battlefield Medicine':'first aid, dealing with immediate injuries',
        'Poison':'ability to recognise and counteract dangerous substances',
        'Accounting':'treasury, profits and expenditures',
        'Trade':'how goods are bought and sold between locations',
        'Production':'national resources and how they are made into goods',
        'Strategy':'the skill of achieving victory on land',
        'Naval Strategy':'the skill to achieve victory at sea',
        'Logistics':'being able to move troops and supplies in a timely fashion',
        'Dance':'knowing the steps and carrying them out with grace',
        'Reflexes':'the ability to respond quickly to surprises',
        'Flexibility':'the ability to stretch and contort without pain',
        'Swords':'the ability to use a blade both for formal duels and deadly force',
        'Archery':'the ability to strike a target at range',
        'Polearms':'the ability to wield a long staff or ceremonial weapon',
        'Running':'ability to move swiftly and surely across land',
        'Climbing':'scaling ropes, rocks, and walls',
        'Swimming':'endurance and speed when crossing water',
        'Horses':'riding and grooming',
        'Dogs':'training, hunting',
        'Falcons':'training, hunting',
        'Meditation':'finding and maintaining your own inner peace',
        'Divination':'interpreting signs from nature of what the future might hold',
        'Lore':'the magical history of Nova',
        'Sense Magic':'the ability to detect mystical power at work',
        'Resist Magic':'defense against mystical powers',
        'Wield Magic':'knowledge and control of your own magical powers',
        }

    class Stat(object):
        instances = dict()
        levelfluff = ()
        def __init__(self, parent, name, varname, levelfluff):
            self.name = name
            self.varname = varname
            self.subgroup = parent
            self.instances[name] = self
            self.levelfluff = levelfluff
            self.unlock = 1000000
            self.unlock_text = None
        def description(stat):
            return stat_descs.get(stat.name,"Studying "+stat.name+' raises '+stat.varname+'.')
        def SetUnlock(stat, val, text):
            stat.unlock = val
            stat.unlock_text = text
        def StudyDescs(stat,oldval,newval):
            ret = []
            oldval = int(oldval/10)
            newval = int(newval/10)
            while oldval<newval:
                if oldval<len(stat.levelfluff):
                    newfluff = stat.levelfluff[oldval]
                    if type(newfluff) is type(apply_mood_bonuses):
                        newfluff = newfluff()
                    ret.append(((oldval+1)*10,newfluff))
                oldval += 1
            return ret

    class Subgroup(object):
        instances = dict()
        def __init__(self, parent, name, varname, n1, v1, f1, n2, v2, f2, n3, v3, f3):
            self.instances[name] = self
            self.name = name
            self.varname = varname
            self.stats = (Stat(self,n1,v1,f1),Stat(self,n2,v2,f2),Stat(self,n3,v3,f3))
            self.group = parent

    class StatGroup(object):
        instances = dict()
        def __init__(self, name, varname, *groups):
            self.instances[name] = self
            self.name = name
            self.varname = varname
            self.groups = []
            for group in groups:
                group = Subgroup(self, *group)
                self.groups.append(group)

    def climbing_100_fluff():
        if flags.get('week36_father_dead',False) or 'week36_father_coma' in flags:
            return "With the aid of your teacher, you manage to climb a stretch of castle wall and into a window."
        return "With the aid of your teacher, you manage to climb a stretch of castle wall and into a window, to your father's chagrin."

    social_skills = StatGroup('Social','social_bonus',
        ('Royal Demeanor','royal_demeanor_bonus',
            'Composure','composure',(
                'You practice deep breathing exercises, learning to find and maintain a sense of inner calm.',
                'You practice positive thinking, maintaining a good self-image, and conditioning yourself to carry on rather than be frustrated by any past misstep.',
                'You practice sitting calmly while your teacher circles around you and makes unexpected loud noises at random intervals.',
                'At your command, your teacher strikes your palm with a leather tawse, and you learn to bear the sting.',
                'You lie on a couch and try to remain relaxed while your teacher smacks your heels with a leather tawse.',
                'You are strapped into tight, heavy armor and made to walk around in it, learning that any attempt at sudden movement will catch painfully or trip you up.  Slow and steady is the way to go.',
                'Your teacher smears your body and clothes with strawberry jam and makes you walk around like that for hours, facing the funny looks and snickers aimed at you without hiding or becoming angry.',
                'You practice walking over smoldering coals with bare feet.  So long as you keep moving steadily and do not panic and freeze or run, you are not burned.',
                'Your teacher gathers up some of the castle staff to shout insults at you, while you practice staying calm (and not bursting into laughter).',
                'Your teacher instructs you in a game of cards, teaching you to bluff with a straight face.',
                ),
            'Elegance','elegance',(
                'You practice walking along a narrow rail, taking each step carefully and focusing on your balance.',
                'You practice standing and walking with books balanced on your head.',
                'You practice the elegant way to hold and sip from a teacup, your pinky slightly extended for balance.',
                'You are strapped into a corset and hoop skirt, and practice walking with these: the corset makes it hard to breathe and twist, and the skirt sways out of control if you move too rapidly.',
                'You practice graceful arm gestures for every motion, from offering your hand for a kiss to taking hold of a banister at the stairs.',
                'You practice eating slowly and with a minimum of mess, chewing each bite a set number of times before swallowing.',
                'You practice standing up, sitting down, and picking up items from the floor.  Bend at the knees, not at the waist.',
                'You practice speaking and laughing quietly, not trying to disappear or go unheard, but focusing your energy into a smaller space so that it draws people closer.',
                'You practice sitting quietly and listening to the conversations of others without becoming bored or restless.',
                'You practice standing in attractive positions, in full costume, and maintaining those poses for long periods of time.'
                ),
            'Presence','presence',(
                "You practice wearing the royal regalia and looking at yourself in a mirror.  Young as you are, you are a queen of the blood.  You are your mother's daughter.  You are a force to be reckoned with.",
                'You stare at yourself in the mirror and practice focusing and transmitting energy with only your eyes, turning the "intensity" of your gaze on and off at will.',

                'You practice using different styles of breathing in order to feel more energetic and to let that energy surround you for others to share.',
                'You plant your feet in a strong stance, imagining that you are a tree, deeply rooted in the earth.  You can feel that power within you and know that you will not be pushed aside.',
                'You practice focusing your attention on individuals as you pass, letting them feel a brief connection with you before you formally acknowledge them with a nod.',
                'You practice being aware of your environment, seeing everything as it transpires around you and feeling that you are in control of it all. ',
                'You practice giving commands to the castle staff, neither asking nor demanding, but telling them what needs to be done.  As long as you believe it to be true, they will as well.',
                'You practice watching people and {b}willing{/b} them to feel your gaze on them.  Inevitably, they will be drawn to you.',
                'You imagine things that you want to happen in the near future, and then convince yourself and others that those things {b}will{/b} happen.',
                'You organise a group of castle staff and coach them through carrying out a complicated, multi-stage task.',
                )),
        ('Conversation','conversation_bonus',
            'Public Speaking','public_speaking',(
                'You practice tongue-twisting sequences of syllables to improve your enunciation.',
                'You take deep breaths and practice speaking loudly and clearly, projecting your voice to every corner of a room.',
                'You memorise lists and sonnets, then recite them for your teacher and any castle staff she can round up to serve as an audience.',
                'Your teacher asks you questions about made-up nonsense, pushing you to improvise answers smoothly and swiftly without having to worry about them being correct.',
                'You read collections of famous historical speeches, and practice saying them in convincingly dramatic fashion.',
                'You borrow the menu for an upcoming banquet and practice delivering it as a dramatic speech to an audience of confused chambermaids.',
                'You learn about debate techniques and practice them by trying to convince a castle gardener why a new fountain would be a good idea. ',
                'Your teacher assigns you to create and memorise a short speech of your own.',
                'Your teacher assigns you to read about a subject, memorise a few good phrases for the beginning and ending of a speech, and then make up the rest on the spot.',
                'Your teacher assigns you to read about a subject, then requires you to answer questions about it on the spot in front of an audience.',
                ),
            'Court Manners','court_manners',(
                'You review the correct greetings for guests according to rank and when to extend your hand to another.  All nobles expect their due honors.',
                'As the person of highest rank within the domain, no one may sit at any formal event unless you give them permission, and no one must ever turn their back on you.  If they do, you are intended to recognise the insult.',
                'You study rules for formal dining, including the proper utensils for different dishes.  As the queen, no one will comment on your mistakes, but they will notice them.',
                'You study the traditions of ballroom etiquette, how to politely accept or defer an offer, and how to avoid the impression of attachment to an individual.',
                'You memorise the correct title for every servant in the castle.  Treating servants with respect ensures good service.',
                "To directly challenge someone's honor is to declare war.  Never make a public accusation of cowardice, treason, infidelity, or murder unless you are prepared to face mortal enemies.  And on that note, you study the etiquette of dueling.",
                'As a monarch you are expected to embody the virtues of honesty, bravery, and generosity.  You should always offer aid to those in need; however, those you aid personally are expected to give you their utmost loyalty even unto death.',
                'You study the forms of written address; how to issue and decline invitations, how to announce an impending visit, and how to correspond with the rulers of foreign domains.',
                'You study the language of flowers, and the secret meanings that can be communicated through the gift of a bouquet.',
                'You study the rules of behavior in foreign courts, so that you may seem at home in any setting.',
                ),
            'Flattery','flattery',(
                "You learn that it's important to make eye contact when saying nice things about someone.",
                'You learn that flattering comments have the best impact when kept short.  Gushing makes people feel awkward.',
                'You learn that it is always better to compliment people for their personality and their choices than their physical attributes.',
                "Visual elements are best to flatter on first meeting; they are expected to be noticed right away.  If you've spent more time with someone, suddenly complimenting their attire will ring false.",
                'Small personal details help make the recipient of your flattery feel that you have truly noticed them, which is always better than a simple "how nice you look".',
                'Most people want to believe that they are successful and well-liked more than they want to believe that they are handsome.  Play to these beliefs and they will be inclined to enjoy your company, even if they should know better.',
                'A certain class of dramatic personality believes utterly that they are ugly and unpopular, even if this is untrue.  Flattering their appearance will make them pull away and mistrust you.  Instead, compliment their intelligence; this tends to be their weakness.',
                'Most people want to believe that they are special and will react well to hints that they are receiving slightly better treatment than others.  However, too-obvious favoritism will stir resentment, and only the vain enjoy it.',
                'The most reliable form of flattery is to convey that you honestly like the target, enjoy spending time with them, and wish them to think well of you.',
                "Imitation is a form of flattery; mirroring someone's gestures and reactions can lead them to subsconsciously trust you and feel that you have a bond.  Be careful not to make this seem like mimicry, which is insulting.",
                )),
        ('Expression','expression_bonus',
            'Decoration','decoration',(
                'You discuss the nature of beauty, looking around at landscapes, objects, and people and comparing their aesthetic elements.',
                'You practice sketching fruits and flowers with charcoal on parchment.',
                'You study the theory of color, how they complement and contrast, and how to select colors to emphasize a mood.',
                'You learn to mix paints and apply them to canvas, capturing the light and color of the castle gardens.',
                'You study the art of floral design, seeing how the proper arrangement of flowers can affect the character of a room or an outdoor space.',
                'You experiment with wax, learning both to build up small amounts and shape them together, and to carve out patterns from larger wax blocks to find the shapes already inside.',
                'You experiment with fashion, trying on different outfits and watching as others do the same, learning how clothing can enhance or diminish certain physical features or give the impression of youth or age.',
                'You practice all the techniques of needlework, from simple mending to dressmaking and embroidery.',
                'You practice designing beautiful outfits from the first scrap of fabric to the last finishing touch of jewelry.',
                "You practice painting miniature portraits, capturing (and in some cases enhancing) each subject's unique beauty."
                ),
            'Instrument','instrument',(
                'You tap out chiming dyads on a glockenspiel, learning the basics of harmony and rhythm.',
                'You learn to play notes and scales on a simple wooden recorder.',
                'You practice with the recorder, learning to recognise tunes that you hear and replicate them.',
                'You practice major and minor scales at the keyboard of a pianoforte.',
                'You study musical notation and begin to play familiar songs by sight on the pianoforte.',
                'You practice complex runs, trills, and transposition on the pianoforte.',
                'You practice the transverse flute, learning how to form a beautiful tone by blowing across the mouthpiece.',
                'You practice the hautbois, learning to apply pressure with your lips to control the vibrations of the double reed.',
                'You practice the harp, learning to play flowing glissandos and arpeggios.',
                'You practice sight-reading complex pieces of music.',
                ),
            'Voice','voice_skill',(
                'You practice deep-breathing exercises to build up your ability to sustain a note.',
                'You learn the differences in resonance between the chest, the head, and the nose.',
                'You learn about different vocal ranges, from the most profound bass to the rare coluratura soprano.',
                'You learn the sol-fa system, a way of expressing a tune where each note is represented by a different syllable.',
                'You practice standing in the correct posture and singing scales to improve your pitch and tone.',
                'You work through exercises in dynamics (going from soft to loud and back again) and agility (singing rapid sequences of notes).',
                'You sing familiar songs in a chorale, focusing on pronunciation and staggered breathing.',
                'You and your teacher practice singing in harmony, feeling the way that notes interact and pulse when not quite in line.',
                'You practice singing canons, learning to maintain focus and timing on your own vocal part even when others around you are singing something quite different.',
                'You practice singing solos, learning to express the emotion of a piece and control the vibrations of your voice.',
                ),),
        )
    physical_skills = StatGroup('Physical','physical_bonus',
        ('Agility','agility_bonus',
            'Dance','dance',(
                'You practice curtseying, standing, and walking across the floor in a graceful manner.',
                'You practice walking on the arm of a partner and following their cues to pause and turn while keeping your eyes closed.',
                'You practice different partnered dance positions - closely held, at a distance, and non-contact - and the appropriate hand placement for each.',
                'You begin practicing dance steps in time to music, quick and slow, turning and weaving.',
                'You work through the standard repertoire of ballroom dancing, being sure you know the basic steps for any dance likely to be required of you in a social setting.',
                'You practice the postures and extensions of solo ballet, learning to stretch and form an elegant line with your body.',
                'You study the secret language of dance and how a story can be told through gestures and positions.',
                'You design your own dance movements to cover the floor, first slowly and then with greater speed.',
                'You practice dramatic movements with a partner - dips, lifts, and tosses.',
                'You practice high-speed spins and turns on pointe, whipping your leg around dramatically.',
                ),
            'Reflexes','reflexes',(
                'Your teacher walks around you, prodding a finger at you slowly in order to train you in blocking those touches without triggering fear or faster breathing.',
                'You practice with a jumprope to increase the speed of your footwork.',
                'You practice solo tennis, hitting a ball against the wall repeatedly in order to train your hand and your eye to react.',
                'You practice running at high speed back and forth over a small area, making quick turns and changes in direction.',
                'You practice tennis against multiple opponents, learning to judge at a glance when a ball is too far away to reach in time.',
                'You practice chasing a small dog through the castle gardens, leaping over uneven stones and dodging through branches.',
                'You practice touch-blocking skills at full speed, deflecting hands before they can reach you.',
                'You practice running through a field dodging balls that are thrown at you from all sides.',
                'You sit quietly in the center of a room, watching out of the corners of your eyes to see people approaching you from a distance.',
                "You practice catching balls that are thrown at you from different directions while you're not looking, so that you have to rely on hearing and instinct to sense the incoming missiles.",
                ),
            'Flexibility','flexibility',(
                'You learn to relax and evaluate the tension in your body, then to practice the different types of motion available to each of your joints: twisting, shifting, and rotating.',
                'You practice circling your arms and making kicking motions with your legs to stretch out your limbs.',
                'You practice bouncing motions with your arms and legs to increase the muscular effect.',
                'You kneel with your hands pressed to the floor, then stretch like a cat, rolling your back up and down.',
                'You practice holding your body in stretched-out poses with the aid of your teacher to support your limbs.',
                'You practice stretching into poses and holding them for short periods of time.',
                'Your teacher holds your limbs in a slightly uncomfortable position for a few seconds, then encourages you to push carefully against the resistance she provides.',
                'You work on achieving a full straddle split, your legs straight and wide.',
                'You arch up into an elegant backbend, then kick over into a standing position.',
                'You practice until you can pull your leg up behind your head.',
                ),),
        ('Weapons','weapons_bonus',
            'Swords','swords',(
                'You take up a wooden sword and practice correct grips and stances.',
                'You practice slow swings to move your blade to precisely-marked targets, building up your muscles and control.',
                'You drill with a partner, attacking and blocking in carefully timed patterns.',
                'You practice moving with a blade - sidestepping, charging, and lunging.',
                'You practice using your blade to disarm opponents or shove them backwards.',
                'You spar with a partner, trading blows while looking for openings to tag each other.',
                'You begin to work with a metal blade, getting the feel for its weight and edge as well as learning how to care for it.',
                'You practice drawing your blade and striking at short notice from a variety of positions.',
                'You learn techniques for thrusting your blade through armor to disable or kill your opponent.',
                'You learn advanced techniques for holding off multiple opponents at once.',
                ),
            'Archery','archery',(
                'You learn how to twist and wax bowstring from a variety of fibers.',
                'You learn to cut, fletch, and tie arrows.',
                'You learn about different styles and sizes of bows - long, short, and recurve.',
                'You learn about caring for your bow - how to store it between uses, string and unstring, and check for damage or wear.  You also learn that you should never "fire" a bow without an arrow on the string.',
                'You strap on protective gear and practice gripping, drawing, and anchoring the bow, before finally loosing a shot.',
                'You practice shooting at clearly marked targets across a flat field.',
                'You practice shooting at targets of different shapes and sizes in mixed terrain.',
                'You practice long-distance shooting, setting arrows into the ground at different ranges.',
                'You practice shooting at moving targets.',
                'You practice shooting targets while you yourself are moving, pulled along in a chariot.',
                ),
            'Polearms','polearms',(
                'You learn about a variety of long weapons, from the quarterstaff to the spear to the halberd and glaive.',
                'You practice walking while carrying a long weapon, getting the feel for its size and weight and learning to maneuver without banging it into anything unintentionally.',
                'You learn the basic stances, grips, and positions for staff fighting, and how to block a blow without crushing your fingers.',
                'You practice standard attacks and sweeps with a long staff.',
                'You practice sparring with a partner using a staff.',
                'You practice special techniques with a staff, such as twirling it or using it to vault.',
                'You practice basic techniques with a long spear, controlling your thrusts to penetrate specific targets.',
                'You practice basic swings with a halberd, building up your arm strength while learning to control the movement.',
                'You practice sparring with a wooden halberd versus a wooden sword, learning the dangers of overextending or allowing your opponent in too close.',
                'You practice with unusual weapons such as the spiked staff, the sword-staff, and the voulge.',
                ),),
        ('Athletics','athletics_bonus',
            'Running','running',(
                "You practice walking at a brisk but comfortable pace for a set length of time every day.",
                "You switch back and forth between a brisk walk and a light, bouncing jog.  Not too fast; you're building endurance rather than speed.",
                "You steadily increase the proportion of time you spend jogging, with shorter breaks of walking to recharge your energy.",
                "You practice jogging solidly for longer stretches of time, and learn how much food and water you need before and after in order to keep your body going.",
                "You learn the proper techniques and clothing for running in different kinds of weather, to avoid frostbite, overheating, or disease. ",
                'You practice running up hills to build leg strength.',
                'You practice running on sand, providing a different kind of resistance for your legs.',
                'You start working in small amounts of faster running into your jogging routine.',
                'You run at your best speed over set distances, then slow down afterwards.',
                'You experiment with carrying different amounts of weight while running, to see how fast you could move for how long with your equipment.',
                ),
            'Climbing','climbing',(
                'You practice climbing up and down fixed ladders, driving out any fear of heights and learning to move swiftly and surely.',
                'You learn to evaluate whether a tree or a branch is safe to bear your weight.',
                'You clamber up and down trees, able to fetch fruit or get a better view.',
                'You practice climbing up and over a wall with the aid of a well-anchored rope, leaning into the wall as you push in with the balls of your feet.',
                'You practice abseiling down a wall, descending with the aid of a rope.',
                'You practice climbing up and down a free-hanging rope, learning to move in rhythm with the rope as it rocks.',
                'You learn how to tie a variety of knots, and which ones are safe to use around the body when climbing.',
                'You learn about different kinds of rock climbing equipment, and how to safely drive in pitons and support ropes.',
                'You practice climbing a simple rock face, learning how to find the most stable grips and footholds, and always keeping three points in contact.',
                climbing_100_fluff,
                ),
            'Swimming','swimming',(
                'You get comfortable in the water, splashing around and holding your breath to go under.',
                'You practice walking and hopping through the shallows, feeling the difference in resistance that the water applies to your movement.',
                'You practice floating on your front and your back, letting the water do the work of holding you up.',
                'You practice treading water, keeping yourself afloat for increasing periods of time.',
                'You learn several different styles of swimming across the water and the leg and arm strokes for each.',
                'You learn styles of swimming to be used underwater, as well as safety warnings for venturing into murky depths.',
                'You practice swimming back and forth over set distances.',
                'You learn about the hazards of swimming in different natural environments, such as river rapids, ocean undercurrents, and winter ice.',
                'You venture out into sea water, feeling the waves and the changes in buoyancy.',
                'You practice swimming in full clothing and even light armor, and also practice removing these items while wet.',
                )),
        ('Animal Handling','animal_handling_bonus',
            'Horses','horses',(
                'You walk around the stables, meeting the royal horses, learning about their breeds and the names for different parts of their anatomy.',
                'You learn about caring for horses: grooming with different brushes and keeping hooves free of stones.',
                'You learn about the different pieces that go into saddles and bridles, how to check for signs of wear, and how to equip and adjust them on a horse.',
                'You learn how to mount and dismount a horse, first with a boost and then from the ground.',
                'You learn how to handle the reins and guide a horse around the field.',
                'You practice different gaits; walking, trotting, cantering, and galloping.',
                'You practice special maneuvers such as backing up or maneuvering in tight quarters.',
                'You practice riding and jumping over small obstacles.',
                'You ride over longer distances and handle natural obstacles as they occur.',
                'You practice guiding the horse using only your knees so that your hands are free for other activities.',
                ),
            'Dogs','dogs',(
                'You visit the kennels and learn about different breeds of dogs.',
                'You learn about dog grooming and the most common diseases and injuries that dogs suffer from.',
                'You learn the standard commands for working with trained hunting dogs and retrievers.',
                'You practice working with trained dogs in a small area, telling them to stay, search, and fetch.',
                'You choose a young puppy and begin raising him to respond to you over all others.',
                'You roam around the castle and grounds with your dog, letting him learn his way while he becomes accustomed to the sights, smells, and sounds of the castle inhabitants.',
                'You begin training your dog to follow simple commands such as following or staying in place.',
                'You train your dog to search for hidden treats, items, and people.',
                'You go for walks with your dog in the woods and invite him to fetch anything interesting that he can find.',
                'You train your dog to perform silly tricks on command.',
                ),
            'Falcons','falcons',(
                'You visit the mews and learn about different kinds of trainable birds, their preferred nesting sites, behavior, and food.',
                'You learn about the fragility of hunting birds and the years of training necessary to develop mastery.  Luckily, your royal falconer does most of the hard work for you.',
                'You learn about the hood and leather jesses, how and when they are worn, and how to keep them maintained and oiled.',
                'You spend time with your chosen bird, speaking to her and letting her get to know you.',
                'You don a heavy leather glove and encourage your bird to hop onto your fist.',
                'You carefully feed tidbits to your bird while she rests on your glove.',
                "You practice walking around holding the bird, attached to you by a short length to ensure she doesn't fly away.",
                "You practice whirling a lure overhead for your bird to catch before calling her back to your hand.",
                "You practice playing with the lure, making it more difficult for the bird so that it takes multiple passes to grab her 'prey'.",
                'You take your bird out for free flights to catch small prey on her own and return it to you.',
                ),),
        )
    Stat.instances['Dance'].SetUnlock(50,"You may now attend Ballroom Dancing on the weekends.")
    Stat.instances['Reflexes'].SetUnlock(30,"You may now play Sports on the weekends.")
    Stat.instances['Horses'].SetUnlock(50,'You may now Hunt on the weekends.')

    def foreign_affairs_20_fluff():
        refusal = True
        if 'week10_battle_loss_soldiers' in flags:
            refusal = False
        elif flags.get('week10_ixion_diplomacy','') in ('pay','punish'):
            refusal = False
        elif flags.get('week10_ixion_diplomacy','')=='bluff' and 'week10_ixion_battle_pending' not in flags:
            
            
            
            refusal = False
        if refusal:
            return 'Four years ago, the Duchess of Hellas tried to foment an insurrection in northern Ixion, just over the Galben River border.  Not only did that fail, but in retaliation, Ixion pushed troops into southern Maree, and they are still refusing to leave.'
        return 'Four years ago, the Duchess of Hellas tried to foment an insurrection in northern Ixion, just over the Galben River border.  Not only did that fail, but in retaliation, Ixion pushed troops into southern Maree.'

    intellectual_skills = StatGroup('Intellectual','intellectual_bonus',
        ('History','history_bonus',
            'Novan History','novan_history',(
            'You read about the history of your domain.  Hundreds of years ago, Nova was the center of a great empire, spanning the length of the western coast as well as a few island territories.  Over time, your influence has waned.',
            "Nova's history involves an endless slew of names and dates.  Even as small as it's become, there are ten dukedoms - no, eleven now - plus the royal line.  You hope no one expects you to memorise every lineage.",
            'No individual may hold more than one dukedom, but nobles seek noble spouses, so titles often come together before being parceled out to heirs.  Your father is Duke of Caloris, and his brother is Duke of Mazomba; Brin, Duchess of Hellas, is the sister of Banion, Duke of Maree, and so on.',
            "Arisse, Duchess of Lillah, is the mother of the Duchess of Mead, the mother-in-law of the Duke of Kigal, and the stepmother of the future Duke of Elath.  People sometimes call her Nova's Eastern Queen.",
            'The Duchy of Sudbury is currently held in regency by Countess Lieke of Dis for her daughter Gwenelle, who is your age.  She inherited the duchy last year upon the death of her father.',
            'The last two rulers before your mother, Queen Fidelia, were your grandmother, Queen Ladesh, and her father, King Fulbert.',
            'About sixty years ago, the Duchess of Merva died with no close heirs, and King Fulbert claimed the lands for the keeping of the crown.  After your mother took the throne, she re-created the duchy and made her brother, your uncle, its Duke.',
            'About two hundred years ago, a great black cloud formed over Nova, bringing cold and sickness.  The sun could not shine, and the air was gritty and foul-smelling.  Many people died, including the queen at the time and most of the high nobility, before the cloud finally dissipated.',
            'Until about six hundred years ago, the capital of Nova was on the shores of Kathre Lake, in southern Caloris.  After that became uninhabitable, a new capital was built here on Lampsi Island.  It was the chaos of that period which triggered the eventual collapse of the empire.',
            'The most famous ruler of ancient Nova was King Latimer.  According to the history texts, he began the policy of "gathering light" which led to the predominance of the Empire.  Unfortunately, the texts don\'t explain what exactly that policy {i}was{/i}.  There\'s a reference, but that volume is missing.'
                ),
            'Foreign Affairs','foreign_affairs',(
                'You study the relationship of Nova and its nearest neighbors.  The borders have been mostly peaceful in recent years, except for the problems with Ixion to the south.  However, trouble may be brewing in Pyrias as well.',
                foreign_affairs_20_fluff,
                'Tombula, to the north, underwent a peasant revolution shortly after you were born.  The nobles either fled or were killed, and the new rulers have so far refused to establish official diplomatic ties with Nova.  While they are not friendly, neither are they enemies, at least not yet.',
                'Southeast lies the domain of Talasse, with which we have enjoyed fairly cordial relations.  Sedna, their chief province, borders the Novan duchy of Elath, and nobles from the two provinces have been known to intermarry.',
                'The duchy of Lillah was not part of the pre-imperial Nova domain, but the western range of the Yeveh nomads.  A faction of Yeveni who wished to settle offered their allegiance willingly to a Novan queen, and their chief was named a Duke.',
                'Because the Lillans are descended from Yeveni castouts who were officially shunned, the Yeveh nomads do not acknowledge that Lillah even exists.  They treat their western border as an invisible wall, and Novan emissaries as travelers from an impossibly distant land.',
                'Over the mountains to the northeast lie the deserts of the Pyrias tribes, who are traditionally hostile to Nova but too lacking in resources to mount a credible threat.  Small groups of Pyrian raiders are sometimes found in Kigal and Sudbury.',
                'The domain of Terrax, far to the south, has warred with Ixion on and off for centuries, even when both were part of the Novan empire.  Your grandmother assisted the Ixionites in putting down the last disagreement thirty-two years ago.',
                'The island domain of Malini was once a small outpost of the Novan empire, but was simply forgotten about in the chaos six hundred years ago.  They were so pleased to have gained their independence without violence that they have remained a strong trade partner to this day.',
                'You learn that in the decline of the Novan empire, slave-raiders from Orcus terrorised the western coastline, until your paternal great-grandfather, then-Duke of Caloris, led a fleet to their capitol and came back with most of their treasury.',
                ),
            'World History','world_history',(
                "You look at a globe of the world, reading names of places so distant you can't remember ever hearing about them, and other areas left blank because no explorer venturing there has ever returned.",
                'You read about the western continent, Jiavar, where civilisation flourished so long ago that the ancestral Novans were still living in caves.  No one knows what became of them; the population vanished without a trace, leaving only their enormous stone buildings.',
                'In the distant past, the Yeveni tribes to the east rode great beasts with spines and tentacles on their heads instead of horses.  The bones of these creatures are sometimes found in Lillah and Mead, and their tusks are valuable to crafters.',
                'You read about the northern continent, Borealis, where the first Lumens in history were recorded, and how the discovery of magic shaped their development.',
                'You read about the hundred-year war which left much of Borealis uninhabitable and created a power vaccuum which would eventually be filled by the growing power of Nova.',
                'Borealis now is mostly made up of tiny domains containing no more than a few village-like settlements each, officially ruled over by shamanic Lumens.  They have few resources and live primarily from the sea.',
                'You read a brief history of the rise and fall of the Novan empire.  There was a time where it seemed likely that Nova would grow to cover the entire world, but it all came apart.',
                'The Novan Empire once had outposts on the western continent, but was driven out six hundred years ago.  The most important domain in that area today is Shanjia.',
                'Until two hundred years ago, Shanjia was not a true domain, but a confederation of trading city-states, each largely independent except for the limited rule of an elected council.  An internal dispute led to the eventual victorious general declaring himself king.',
                'In recent years, the queen of Shanjia has pursued an expansionist policy, conquering several smaller domains nearby and bringing them under her control.',
                ),),
        ('Intrigue','intrigue_bonus',
            'Internal Affairs','internal_affairs',(
                'Until you have children of your own, your maternal uncle, the Duke of Merva, is next in line for the crown, and after him would be his daughter, your cousin Charlotte.',
                "Your maternal uncle's wife, the Countess Nix, claims kinship to the old Merva line and originally asked your mother for title to the duchy.  However, no one could verify her lineage.  As a compromise, your mother created her brother Duke of Merva.",
                'The last Duke of Mead was the older half-brother of the current Duchess.  His reign was brief and highly scandalous - he defied tradition to pledge himself as the lifemate of the old Duke of Ursul, then broke that off only a year later.  He retired into seclusion and died still unwed.',
                "The Duke of Maree has paid suit to the Duchess of Ursul to no avail.  The Duchess's brother is opposed, as he will inherit if she dies childless.  Your agents suspect the Duchess of Ursul is actually more interested in the Duchess of Hellas.  Neither has ever been linked to a man.",
                "Countess Lieke of Dis married the old Duke of Sudbury, who was more than twice her age, then divorced him as soon as she'd borne him an heir in order to be free to marry another.  It was considered shockingly rude by the general nobility, but the old Duke apparently had no objection.",
                "The Countess of Dis is now married to the disinherited third sibling of the Duke of Maree and the Duchess of Hellas.  Currently, both Duke and Duchess are unwed.  If either dies without heir, a title may still pass to the Countess' husband.",
                'Several generations back, the rulers of Elath and Sedna in neighboring Talasse married.  The citizens of Elath objected to this foreign influence, and the resulting heir died in suspicious circumstances, after which the title was passed to a distant branch of the family rather than another child of the Elath-Sedna union.',
                'There were many dark rumors about the second husband of the Duchess of Lillah, possibly because he was a commoner.  It was whispered that he once assaulted the young Duchess of Elath before her untimely marriage and demise.',
                'After years of marriage and three children, the Duchess of Lillah divorced her second husband and refused to say why.  Shortly afterwards, he was found dead in a nearby forest.  The Duchess of Lillah and her son the Earl of Io have been estranged ever since.  The Earl of Io now lives with his sister, the Duchess of Mead.',
                "After the last Duke of Mead went into seclusion, he hired a stream of attractive young servants who had to be frequently replaced after injuries and 'accidents'.  He eventually died by falling from a high tower window, which his family covered up.  But was it suicide they were hiding, or murder?",
                ),
            'Foreign Intelligence','foreign_intelligence',(
                'The current Duke of Sedna is twenty-six years old and unmarried.  He might be considered a good marriage prospect for you if you desire stronger ties with the domain of Talasse.',
                'The domain of Shanjia, across the sea to the west, has been steadily increasing in size, and now controls a wide range of coastline as well as most of the navigable rivers.',
                'The political disruption in Tombula in recent years has caused a disruption in their chocolate production, which is to the benefit of Nova, particularly the duchy of Kigal.',
                'Since their recent revolution, the Tombulans have twice begun gathering troops on the Novan border.  Both times, their camps were struck by fierce storms and earthquakes, and they decided to give up on the idea.',
                'Pirates are once again operating out of Orcus, although they are currently sticking to the northern seas and no threat to Nova.  However, if they turn to slave raids, the Borealans may be quite vulnerable.',
                'Agents who have visited Borealis report that all known "Lumen Shamans" seem to have no magical powers at all, and perform their ritual displays with show and trickery.',
                'Rumor has it that the mother and older sister of the last Duchess of Elath were assassinated twenty years ago by agents from Sedna, which is why she, as sole remaining heir, was married off so young.',
                'Rumor has it that the Prince of Terrax was humiliated by the public dissolution of his betrothal to an heiress after she declared him a coward.',
                'The queen of Shanjia is wedded to a non-noble, a court musician whom she initially took as a consort, barring any offspring from inheriting the throne.  She has since passed new laws to give not only their children but also the man himself an equal claim to the crown.',
                'Rumor has it that the "King" of Shanjia has become the true power behind the throne, and that he may also have the powers of a Lumen.  He is a controversial figure within the domain, but ministers who speak against him have been known to disappear.',
                ),
            'Ciphering','ciphering',(
                "You practice reading words whose letters have been arranged in reverse order - the simplest of transpositions, which anyone literate can puzzle through if they try, but sometimes useful to hide information {i}thg is nia lpni{/i}.",
                'You practice shifting substitution ciphers, where each letter is replaced by one a few steps further along the alphabet, so that "cake and pie" becomes "fdnh dqg slh".',
                'You practice random substitution ciphers, where the normal alphabet is replaced by one in jumbled order.  This is harder to decode, but most people need a written substitution chart to read or write it, and that chart can be lost or stolen.',
                'You practice complex transposition ciphers, where messages are written down in columns or lines and then reorganised into scrambled words.  This means that both an encoded and a plaintext written copy exist, which can be insecure.',
                'You practice adding code to your ciphers - that is, replacing words with other words, such as "handle" for "duke", before changing the letters in the message.',
                'You memorise special cipher alphabets where each letter is replaced by a symbol.  Once these are memorised, you will not need to write down cipher sheets, and if the symbols do not look like letters they can be hidden in decorations.',
                'You study an ancient book that has a list of thousands of words and pictograms for each of them.  In the past, these were used for important messages, but only trained bards could effectively memorise enough symbols to handle the codes efficiently.',
                'You learn to manipulate special boxes and jewelry with secret compartments to hide messages.  A rare few have locks almost as complicated as the ciphers themselves!',
                'You learn that the more you use a code, the easier it is for enemies to break it; the most secure cipher is one that is only used for a single message.',
                'You learn to use special codewheels to create rotating ciphers which can only be decoded with another, matching set of codewheels.',
                ),),
        ('Medicine','medicine_bonus',
            'Herbs','herbs',(
                "You learn that willow bark can be used to relieve aches and fever.",
                'You learn that feverfew can be used to reduce tension and headaches.',
                'You learn that oil of cloves, rubbed on the skin, can relieve pain, particularly in teeth.',
                'Sage has a variety of health benefits: it keeps meat from spoiling, aids digestion, improves thinking, and may even help to bring color back into gray hair.',
                "Calendula flowers can be used in soothing teas as well as skin lotions.  It is also said to provide visions of one's secret enemies if worn under the light of a full moon.",
                'Comfrey can be used to help mend broken bones.  However, it is also slightly poisonous in large amounts and should not be eaten.',
                'Burdock leaves can be used as a poultice to draw out infection.  The roots can be used to flavor a kind of beer, and the stalks can be eaten.',
                'The herb valerian calms anxieties and helps bring restful sleep.  It is very popular with the nobility.',
                'The herb known only as "savory" comes in both winter and summer varieties.  Both are useful in treating wasp stings, coughs, and internal gas.  They also make a good flavoring for food.  Summer savory is an aphrodisiac, while winter savory reduces sexual desire.',
                'Jelly made from the berries of the elder tree can cure many illnesses.  However, only druids may safely harvest from elder trees; others will be cursed by its touch.  Properly treated, elderwood makes staves and pipes for religious ceremonies.',
                ),
            'Battlefield Medicine','battlefield_medicine',(
                'You learn that wounds, even minor ones, should be washed as soon as possible to prevent dirt from growing under the skin.',
                'You learn that blood loss wastes life energy.  Bleeding should be stopped through bandages, pressure, and elevation.',
                'You learn that minor burns should be cooled, washed, and gently wrapped to keep them clean, like a cut.  Major burns and scalding such as boiling oil are untreatable on the battlefield.',
                'You learn that soldiers should never sleep in damp clothes or on damp ground, this is unhealthy.',
                'You learn that latrines, food waste, and burials must be kept far away from living soldiers to avoid spreading disease.  Holes should be dug deep and covered after use.',
                'You learn that some wounds need to be sewn closed.  The needle should first be cleaned by holding it in a flame for a minute or two.  Fire should not be applied to the wound; it will make it worse.',
                'You learn that piercing arrows should never be pushed through the body; that will make the injury worse.  Cut very carefully with a sharp blade to dig the arrowhead out without causing large tears in the flesh.',
                'You learn that broken bones should be immobilised with wooden splints to prevent them from moving around.  The straight wood will encourage the bone to grow straight.',
                'You learn about situations where a crushed or rotten limb must be removed in order to save the rest of the body.',
                'A blow to the chest may create a sucking wound which stops the patient from breathing.  A special wax bandage is needed to keep air from passing through the wound.',
                ),
            'Poison','poison',(
                'The first treatment for most ingested poisons is to purge the stomach by forcing the victim to eat powdered charcoal, which can absorb dangerous substances.',
                'Certain poisons will counteract each other, such that either on their own will kill the victim, but carefully applying a matching amount of the other will cure.',
                'If a victim is stabbed with the poisoned spine of a sea urchin, the spine must be removed carefully and the affected area soaked in very hot water in order to cook out the poison.',
                'It is possible to become immune to the venom of a particular snake by routinely ingesting very small amounts.  However, this protection is temporary and will not provide any help against other snakes.',
                "Cinnabar dust causes tremors, anxiety, and eventually death if ingested over a long term.  This is mostly a problem for miners, but it can be dangerous if it is routinely added to someone's food.  There is no cure, but most will slowly recover if they have no more dust.",
                'The herb tansy is a mild poison with particular effect on lower forms of life.  Rubbed on the skin, it repels insects.  Drunk as a tea, it drives out worms from the stomach.  Unfortunately, this sometimes makes people very ill.',
                'Belladonna berries are purple, juicy-looking, and sweet.  Eating a handful of them causes blindness followed by death.  It can be treated very carefully with a paste of calabar beans, which is also poisonous.',
                'The flower known as "black sun" creates a poison which induces violent madness in the victim.  In larger doses it produces the same results as belladonna.',
                'The foxglove flower is a dangerous poison.  Chewing the leaves or drinking water in which they have been soaked is likely to be fatal.  Symptoms include dizziness and yellowed vision.  Powdered epsomite is the only known antidote.',
                'The purple flower known as "woman\'s bane" is a dangerous poison with no antidote.  Touching it causes the body to go cold, then numb, then die within hours.  A rapid charcoal purge may sometimes save the victim.',
                ),),
        ('Economics','economics_bonus',
            'Accounting','accounting',(
                'You brush up on basic mathematics with the help of an abacus.',
                'You study the manipulation of larger quantities through direct calculations, using written numbers instead of an abacus.',
                'You study moneylending and the controversies involved in charging interest.  According to the druids, one should always return more than one is loaned, or else the debt gave no value to the world.',
                'You study bookkeeping and the art of notating incomes and expenditures, as well as how to determine the amount of funds a solvent business needs to keep on hand in order to continue functioning.',
                "You learn about the concept of 'diminishing returns', a point after which spending more on a particular project fails to improve it as much as previous spending did.",
                'You study taxation, and learn about how past monarchs demanded too much and drove peasants into ruin in order to collect it.  Other monarchs demanded too little and drove whole domains into ruin by lacking the funds to sustain and defend them.',
                "You study the standard operating costs of the domain's military and the amounts needed to commission new ships, soldiers, and knights.",
                'You study the art of laying customs duties, and how those tariffs can affect the flow of goods in and out of the country.',
                'You study the costs and benefits of public education and health provisions.',
                'You study the effects of minting more coin to cover economic shortages.',
                ),
            'Trade','trade',(
                'You learn that even the smallest of villages has a central market where locals can trade what they have grown or made with others who have different skills.',
                'You learn that individual peddlers travel between villages and cities, some on foot with packs and mules, others riding horses or wagons.  Sometimes different wagons group together to form a caravan.',
                'The most important trade route in the domain is the Cavalla River.  It travels through the center of your lands, and almost every duchy contains tributaries that feed into the Cavalla, allowing goods to be shipped along it by boat.',
                "Much of the domain's trade comes in from the western ocean.  The capital city, and your castle, are located on an island near the mouth of the Cavalla River where it meets the sea.  That makes this the most important location for trade in the domain.",
                'The second most important seaport in the domain is Ursulia, on the Theku Bay.  Ursul is the only duchy with no access to the Cavalla River; they send their goods south to you by ship.',
                "Over a hundred years ago, a canal was constructed through eastern Lillah so that ore from Elath could be safely transported past the rapids of the upper Cavalla River.  The Duchy of Lillah financed the canal's construction and still receives a toll for every boat which passes through.",
                'The rise of annual fairs helps draw craftspeople and performers to different locations around the domain at different times of year, ensuring wide access to a variety of goods and merchants.  However, this also diminishes the power of the capital and the guildmasters.',
                "Disruption of sea trade would be disastrous.  The navy keeps regular patrols against pirates, and a lookout is always maintained at Shepherd's Point to warn of enemy approaches.",
                'It is possible for small locations to be self-sufficient by making a wide range of goods, but if each location focuses on making fewer kinds of goods which they can produce more efficiently, the overall amount of goods increases.',
                'Trade in this domain has always focused around water.  However, if more and better roads were built, the Duchy of Lillah could gain a lot through overland travel to and from the east.',
                ),
            'Production','production',(
                'You learn that Sunset Bay off the coast of duchy Mazomba is a prime location for fishing.',
                'You learn how farmers in the Duchy of Maree rotate between fields for raising crops and fields that lie fallow.',
                "You learn that most of the domain's iron is mined in Sudbury and transported west by the Gowan River to the Cavalla.",
                'You learn that the hilly terrain in Hellas is no good for growing most crops, but is excellent for vineyards and migratory flocks of sheep and goats.',
                'You learn that gold and other precious minerals are mined in the mountains of Elath.',
                'You learn that wool from Hellas travels north to cotton-growing Mead, where quality cloth is created and dyed.',
                'You learn that sand from Maree travels north to Caloris where it is crafted into glass.',
                'You learn that the forests in Ursul are regularly harvested for timber, but trees in Kigal are left to grow, because in their shade grow the smaller trees whose seeds produce coffee and chocolate.',
                'You learn that an enclave of druids gather herbs from Merva and Mazomba, wine from Hellas, and honey from Mead, in order to make the most valuable medical elixirs.',
                'You learn about the secret combination of metals that must be carefully heated and worked to create wootz steel for top-quality swordsmithing.',
                ),),
        ('Military','military_bonus',
            'Strategy','strategy',(
                'You study the strengths and weaknesses of different weapons in battle formations.',
                'You study the effects of battle stress on troops, and how morale can turn the tide of combat.',
                'You study military recruitment and the importance of training and motivation in making soldiers who can trust and depend on each other.',
                'You learn about how units reinforce each other in the field, gaining strength through proximity and the covering of weaknesses.',
                'You study the effects of different kinds of battle terrain for both offense and defense.',
                "You study the power of ranged weapons, from arrows to thrown fire and sand, and how the threat of such attacks can shift the enemy's response.",
                'You study the use of cavalry in battle, as well as the costs and benefits of traveling with large animals.',
                'You study the effects of a strong hierarchy on military organisation and the ability of troops to respond to changing situations.  Communication across an army can be difficult; disrupted signals can lead to chaos.',
                'You study famous battles: the disasters and the mistakes which created them, and the turning points in larger conflicts and why they made a difference.',
                'You study the concept of "defeat in detail" and how an army can be destroyed by crushing small parts one at a time rather than attacking it all at once.',
                ),
            'Naval Strategy','naval_strategy',(
                'You learn that the sea is not something you hold, it is something you travel across.  Naval strategy ensures your free travel while denying it to your enemies.',
                'You study different kinds of ships - their names, designs, and the number of crew needed for each.',
                'You study different kinds of ships - their speed, maneuverability, and standard complement of weapons.',
                'You learn about the requirement for all civilised sailors to rescue the crew of a sinking ship, even an enemy.',
                'You learn about the challenges to naval warfare posed by unpredictable weather, as well as the dangers of sailing too close to an unknown coastline.',
                'You learn about the use of ships in transporting ground soldiers between locations.',
                'You study the cost, time, and materials required to construct new ships. ',
                'You study blockades, both setting them and breaking them.',
                'You study the effect of cannons against coastal installations such as enemy docks and seaside villages.',
                'You study the difficulty of a sneak attack at sea, and ways that it can be achieved.',
                ),
            'Logistics','logistics',(
                'You learn about the types and amounts of food required for an army on the march, and how long they will remain edible.',
                'You study the kinds of equipment that soldiers need available, such as bedding, weapons, armor, medicine, bandages, and the tools to repair anything damaged.',
                'You study different kinds of transport - animals, wagons, sledges, ships, boats, and boots.',
                'You learn about the support costs created by support - the more equipment you have, the more people and animals are needed to move them, and then those people and animals also need to be fed and equipped.',
                'You learn about the difficulty of obtaining new supplies from the field.  Enemy civilians may hide or destroy supplies rather than let them fall into your hands, and friendly civilians may not stay friendly if robbed.',
                'You study how to determine when to jettison or destroy excess goods for speed, and how to avoid overreaching.',
                'You learn about how to calculate enemy war preparations based on the movement of goods within their lands.  Armies do not spring up full-formed overnight.',
                'You study the benefits of looting as a troop motivator versus the negative effect on civilian populations.',
                "You learn to calculate how effective military strength wanes over distance from a 'home' position, as it becomes more difficult to put pieces into play.",
                'You learn how to delay the advance of an invading force by disrupting their transport and communications.',
                )),
        )
    Stat.instances['Strategy'].SetUnlock(40,'You may now tour the Barracks on the weekends.')
    mystical_skills = StatGroup('Mystical','mystical_bonus',
        ('Faith','faith_bonus',
            'Meditation','meditation',(
                'You practice assuming a sitting position that allows you to be relaxed and tranquil without being so relaxed that you are likely to fall asleep.',
                'You close your eyes and relax every muscle of your body in turn, letting that feeling travel down through you from your head to your fingertips and toes.',
                'You take slow, deep breaths, letting that air move through your body, feeling it give you life and energy.',
                'You stare into a polished crystal ball and relax, letting your mind wander.',
                'You close your eyes and visualise the crystal ball floating in front of your eyes.',
                'You close your eyes and visualise a crystal ball floating through the air, moving past your eyes and into your mind, filling you with light.',
                "You learn to visualise the space around you so that you can 'see' the whole room with your eyes closed.",
                'You discover that if you put yourself into the right frame of mind, your entire body begins to glow faintly.',
                'You discover that if you put yourself into the right frame of mind, you really {i}can{/i} see with your eyes closed.',
                'You discover that if you put yourself into the right frame of mind, you can sense things happening in nearby rooms, even behind closed doors.',
                ),
            'Divination','divination',(
                'You learn that the gods cannot be forced to divulge information about the future, and that the most powerful omens are those which arrive unexpectedly.',
                'Dropping your favorite plate is bad luck.  A statue spontaneously shattering is a bad omen.',
                'You read about well-known signs of bad fortune: wells turning sour, dry lightning, strange fish caught in nets, malformed babies being born, and so on.',
                'You read about signs that have presaged famous disasters, such as the seas running red before the Doomshadow fell upon Nova two hundred years ago.',
                "You read about King Latimer, and how he knew he was destined for greatness when he saw the shape of a crown in a spider's web.",
                'You read about animal omens, in particular the flights of birds.',
                'You learn about signs which sometimes appear in grounds or leaves at the bottom of a cup.',
                'You study the interpretation of dreams, with warnings that dreams are easily forgotten, misremembered, or warped by thoughts and desires rather than true vision.',
                'You study the stars and learn about the omens they hold, with warnings that the stars are seen by all and their portents may not be meant for you.',
                "You learn that priestesses have other ways of requesting omens from the gods, but that they won't share them with someone not initiated into the mysteries.",
                ),
            'Lore','lore',(
                "Only a Lumen can channel magic, and only with the help of an attuned crystal.  The ability to control a crystal seems to be inherited, so crystals can be passed from parent to child... upon the Lumen's death.",
                'The kings and queens of Nova have all been Lumens for centuries, but in modern times, magic is only used for ceremonial occasions and the direst of emergencies.',
                'Long, long ago, the continent of Borealis was ruled over by a single Witch-King, until a rival line of Lumens challenged for the crown.  The resulting war went on for a hundred years with powerful spells that damaged the land so badly that even now, no plants will grow.',
                'Legend has it that long ago, a horde of Yeveni on the back of tentacled monsters rode into the valley of Mead laying waste to all in their path.  Their conquest was only halted when a Lumen raised a great flood to drown the invaders.',
                'Legend says that the island domain of Malini was once a single island instead of a cluster, until an invading Novan queen raised a terrible pillar of fire that shattered the land into pieces.',
                'At the height of the Novan Empire, all the major Dukes and Duchesses were Lumens, and they conquered their enemies with beams of light and terrible summoned monsters.  Those monsters eventually broke loose, killing their captors and destroying the Old Capital on Kathre Lake.  The resulting chaos shook the Empire.',
                'Two hundred years ago, a great force of darkness covered Nova, threatening to wipe out all life in the domain.  It took the self-sacrifice of the Queen and her complement of Lumens to defeat that doom.  Only the Duke of Ursul refused to join in the defense and therefore survived.',
                "A Lumen once tried to lift the curse from an enchanted spring whose water was poisonous and glowed green.  After dispelling the magic, she tasted the water and fell dead - the green glow was a not a curse, but a spell placed by a Lumen long before to warn everyone away from the spring's natural poison.",
                'A Lumen may willingly surrender control of his or her magic to another.  This was how the Novan Empire came to dominate the world - a growing force of Lumens focused on a single ruler, granting that King or Queen immense power.',
                'It is now believed that strong magical power attracts danger.  Therefore, after the doomshadow was banished, the crystals of the fallen Dukes and Duchesses were destroyed.  Only the crown - and the duchy of Ursul - maintain active Lumens.',
                )),
        ('Lumen','lumen_bonus',
            'Sense Magic','sense_magic',(
                "You close your eyes and learn to feel the magic inside you.",
                "You practice using small amounts of magic and feeling that power outside of yourself.",
                "Your mentor summons up magical energies to strike the nearby ground so that you can learn to sense someone else's spells in use.",
                "You close your eyes and call out when you detect your mentor casting a silent spell beside you.",
                "You learn to detect ongoing enchantments, such as blessed weapons that can do magical damage.",
                "You learn to tell the difference between different kinds of magical signatures, so that you can tell roughly what a spell you detect is meant to achieve.",
                "You expand your magical perceptions to give you some idea of where a detected spell was cast from, and how long ago.",
                "You learn to detect the latent power that signifies a Lumen even when he or she is not actively working magic.",
                "You expand your senses, learning to detect spells and magical creatures at a greater distance.",
                "You learn to detect lingering traces of strong magic from the past, even when the spell has long since completed.",
                ),
            'Resist Magic','resist_magic',(
                "You increase your awareness of your own thoughts and emotions, making it more difficult for mind-affecting magic to twist your reactions.",
                "You learn to consciously project a magical field through your thoughts, blocking outside magic from touching your mind - but only when you have the energy to consciously resist.",
                "You gain innate resistance to light and dark - you can now see in the blackest caves or stare into the sun without going blind.",
                "You learn to consciously project a magical shield around your body, blocking intrusion; a powerful technique, but you can't keep it up for long.",
                "You gain increased resistance against heat and cold, becoming comfortable in different weather and environments (and able to sip hot soup without burning your tongue!)",
                "You learn how to quickly flare magical shields around you to deflect an incoming attack. This uses much less energy than a constant shield, but it requires good timing to be effective.",
                "You learn how to maintain a low-level deflection field, so that magical attacks not directly targeted at you will slide harmlessly aside. This doesn't need much power, so you can keep it up for long periods of time.",
                "You learn how to directly counter offensive magic with your own power, so that you can 'burn out' a spell that someone else has cast. This is very dangerous if the other spell is too powerful!",
                "Your increased skill and power gives you innate resistance to mind-affecting magic.",
                "Your understanding of the flow of power gives you increased resistance to damage caused by magic, even without a shield. You can still be hurt, but less than an ordinary human would be.",
                ),
            'Wield Magic','wield_magic',(
                "You learn to summon a small glowing light which you can then move around independently.",
                "You learn how to cast rays of white light which can banish shadows and blind your opponents.",
                "You learn to create tiny discs of solid light which can fly through the air and cut into targets.",
                "By concentrating, you can create a wave of discontent which panics or enrages animals in the area.",
                "You learn to create a blade of solid light, which you can wield like a sword to slice through flesh and stone alike.",
                "You learn to direct a beam of searing light through the end of a staff, burning whatever you point at.",
                "By concentrating, you can create a wave of discontent which panics, confuses, or enrages other people around you.",
                "You learn to shape light into images of things that are far away, or things that don't exist at all.",
                "You learn to create a powerful explosion of light, burning those caught within and blinding others who look at it.",
                "You learn how to make use of images to wield your other powers at a great distance.",
                )),
        )
    def unlock_lumen_powers():
        global lumen_unlocked
        lumen_unlocked = True
        global pre_lumen_meditation
        pre_lumen_meditation = meditation_
        checklist_unlock('lumen')

    def update_adjusted_stats():
        global composure
        composure = composure_
        global elegance
        elegance = elegance_
        global presence
        presence = presence_
        if current_outfit=='royal_demeanour':
            composure += 10
            elegance += 10
            presence += 10
        global public_speaking
        public_speaking = public_speaking_
        global court_manners
        court_manners = court_manners_
        global flattery
        flattery = flattery_
        if current_outfit=='conversation':
            public_speaking += 10
            court_manners += 10
            flattery += 10
        global decoration
        decoration = decoration_
        global instrument
        instrument = instrument_
        global voice_skill
        voice_skill = voice_skill_
        if current_outfit == 'art':
            decoration += 10
            instrument += 10
            voice_skill += 10
        global dance
        dance = dance_
        global reflexes
        reflexes = reflexes_
        global flexibility
        flexibility = flexibility_
        if current_outfit=='agility':
            dance += 10
            reflexes += 10
            flexibility += 10
        global swords
        swords = swords_
        global archery
        archery = archery_
        global polearms
        polearms = polearms_
        if current_outfit=='weapons':
            swords += 10
            archery += 10
            polearms += 10
        global running
        running = running_
        global climbing
        climbing = climbing_
        global swimming
        swimming = swimming_
        if current_outfit=='athletics':
            running += 10
            climbing += 10
            swimming += 10
        global horses
        horses = horses_
        global dogs
        dogs = dogs_
        global falcons
        falcons = falcons_
        if current_outfit=='animals':
            horses += 10
            dogs += 10
            falcons += 10
        global novan_history
        novan_history = novan_history_
        global foreign_affairs
        foreign_affairs = foreign_affairs_
        global world_history
        world_history = world_history_
        if current_outfit=='history':
            novan_history += 10
            foreign_affairs += 10
            world_history += 10
        global internal_affairs
        internal_affairs = internal_affairs_
        global foreign_intelligence
        foreign_intelligence = foreign_intelligence_
        global ciphering
        ciphering = ciphering_
        if current_outfit=='intrigue':
            internal_affairs += 10
            foreign_intelligence += 10
            ciphering += 10
        global herbs
        herbs = herbs_
        global battlefield_medicine
        battlefield_medicine = battlefield_medicine_
        global poison
        poison = poison_
        if current_outfit=='medicine':
            herbs += 10
            battlefield_medicine += 10
            poison += 10
        global accounting
        accounting = accounting_
        global trade
        trade = trade_
        global production
        production = production_
        if current_outfit=='economics':
            accounting += 10
            trade += 10
            production += 10
        global strategy
        strategy = strategy_
        global naval_strategy
        naval_strategy = naval_strategy_
        global logistics
        logistics = logistics_
        if current_outfit=='military':
            strategy += 10
            naval_strategy += 10
            logistics += 10
        global meditation
        meditation = meditation_
        global divination
        divination = divination_
        global lore
        lore = lore_
        if current_outfit=='faith':
            meditation += 10
            divination += 10
            lore += 10
        global sense_magic
        sense_magic = sense_magic_
        global resist_magic
        resist_magic = resist_magic_
        global wield_magic
        wield_magic = wield_magic_
        if current_outfit=='lumen':
            sense_magic += 10
            resist_magic += 10
            wield_magic += 10

label init_stats:
    python:
        weeknum = 0
        composure_ = elegance_ = presence_ = 0
        public_speaking_ = court_manners_ = flattery_ = 0
        decoration_ = instrument_ = voice_skill_ = 0

        dance_ = reflexes_ = flexibility_ = 0
        swords_ = archery_ = polearms_ = 0
        running_ = climbing_ = swimming_ = 0
        horses_ = dogs_ = falcons_ = 0

        novan_history_ = foreign_affairs_ = world_history_ = 0
        internal_affairs_ = foreign_intelligence_ = ciphering_ = 0
        herbs_ = battlefield_medicine_ = poison_ = 0
        accounting_ = trade_ = production_ = 0
        strategy_ = naval_strategy_ = logistics_ = 0

        meditation_ = divination_ = lore_ = 0
        sense_magic_ = resist_magic_ = wield_magic_ = 0
        update_adjusted_stats()

        cruelty = 0
        commoner_approval = 0
        noble_approval = 0
        lassi = 10000

        unlocked_outfits = set()
        update_bonuses()


        readback_log_line = []
        readback_log_data = []


        unroller.last_save_caption = ''

        if not persistent.game_successfully_started_in_gl:
            if renpy.get_renderer_info()['renderer']=='gl':
                persistent.game_successfully_started_in_gl = True
    return

init python:

    def study(activity):
        global new_outfits
        stat = Stat.instances[activity]
        low = 100
        activity_translation_dict = dict()
        subgroup_translation_dict = dict()
        if (persistent.language is not None) and persistent.language in subgroup_translations:
            subgroup_translation_dict = subgroup_translations[persistent.language]()
        if (persistent.language is not None) and persistent.language in activity_translations:
            activity_translation_dict = activity_translations[persistent.language]()
        
        for famstat in stat.subgroup.stats:
            low = min(low,eval(famstat.varname+'_'))
        if low<25:
            cap = 50
        else:
            cap = 100
        code = ('global '+stat.varname+'_\n'+ 
            'old_value='+stat.varname+'_\n'+
            'gain = max(0,2+'+stat.subgroup.varname+'+'+stat.subgroup.group.varname+')\n'+
            'gain *= 5\n'+
            'triedgain = gain\n'+
            stat.varname+'_ += gain\n'+
            'if '+stat.varname+'_>cap:\n'+
            '    '+stat.varname+'_=cap\n'+
            '    gain=cap-old_value\n'+
            'value = '+stat.varname+'_\n')
        exec code in globals(),locals()
        fluff = stat.StudyDescs(old_value,value)
        newlow = 100
        for famstat in stat.subgroup.stats:
            newlow = min(newlow,eval(famstat.varname+'_'))
        if (stat.subgroup.name not in unlocked_outfits) and low<25 and newlow>=25:
            unlocks = _('You have unlocked a new outfit!\n')
            unlocked_outfits.add(stat.subgroup.name)
            new_outfits += 1
        else:
            unlocks = ''
        if old_value<stat.unlock and value>=stat.unlock:
            unlocks += _(stat.unlock_text)
        activity_to_show = activity_translation_dict.get(activity, activity)
        subgroup_to_show = subgroup_translation_dict.get(stat.subgroup.name, stat.subgroup.name)
        if triedgain!=gain:
            if unlocks:
                unlocks += '\n'
            if cap==50:
                unlocks += _('Your skill in %(activity)s is now 50.  You may not increase this skill until your other %(subgroup)s skills are 25 or higher.')%dict(activity=activity_to_show, subgroup=subgroup_to_show)
            elif cap==100:
                unlocks += _('You have nothing more to learn about %s.')%activity_to_show
        elif not fluff:
            fluff = _("You are too "+mood+" to focus properly on this subject right now.")
        return (activity, gain, fluff, unlocks, value)

    def text_size(s):
        return Text(s).render(1024,128,0,0).get_size()

    def text_width(s):
        return Text(s).render(1024,128,0,0).get_size()[0]

    def split_line_w(s, w, renderedw):
        maxidx = len(s)
        ret1 = ''
        
        idx = int((float(w)/renderedw)*len(s))
        idx_a = s.find(' ',0,idx)
        idx_b = s.find(' ',idx)
        if idx_a==-1:
            idx = idx_b
            if idx_b==-1:
                idx = idx
        else:
            idx = idx_a
        last_idx = 0
        last_width = 0
        current_width = w+1
        while True:
            new_w = text_width(s[:idx])
            if new_w<=w:
                last_idx = idx
                last_width = new_w
                minidx = idx+1
            else:
                maxidx = idx-1
            idx = s.find(' ',minidx,maxidx)
            if idx==-1:
                while s[last_idx]==' ':
                    last_idx += 1
                return s[:last_idx],s[last_idx:]
        
        
        
        
        
        
        
        
        
        
        
        print 'sl now',sl

    def tilassi(num=None):
        if num is None:
            num = lassi
        rem = num % 1
        return int(rem*100)
    num_words = ('zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty')
    tens = ('','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')
    def readable_number(i):
        if persistent.language is not None:
            if persistent.language in readable_number_translations:
                return readable_number_translations[persistent.language](i)
            return str(i)
        
        
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

    def treasury_total_str():
        las = int(lassi)
        til = tilassi()
        d = dict(lassi=readable_number(las))
        if abs(las)>1:
            d['las_s'] = _("%(lassi)s gold lassi")%d
        else:
            d['las_s'] = _("%(lassi)s gold la")%d
        
        if til>0:
            d['tilassi_s'] = readable_number(til)
            if til>1:
                return _("%(las_s)s and %(tilassi_s)s silver tilassi")%d
            else:
                return _("%(las_s)s and %(tilassi_s)s silver tila")%d
        return d['las_s']

init:
    image studybg = im.Composite((1024,600),
        (0,0),'schedulebg.jpg',
        (59,46),'ui/big_ribbonbox.png')

transform study_fluff_fade:
    on show:
        alpha 0.0
        pause .1
        linear 1.0 alpha 1.0

screen study_fluff:
    default size = 15
    vbox xpos 385 ypos 120 at study_fluff_fade:
        if type(study_results[2]) in (str, unicode):
            text study_results[2] style style.studyfluff size size
        else:
            for fluffitem in study_results[2]:
                hbox:
                    text (str(fluffitem[0]) + ':') style style.studyfluff size size
                    null width 10
                    text _(str(fluffitem[1])) style style.studyfluff xmaximum 450 size size
            if not study_results[2]:
                text _('Studying...') style style.studyfluff

init python:
    def study_fluff_results_between(fluffs, minheight, maxheight):
        toshow = []
        y = 0
        for fluff in fluffs:
            h = Text(_(fluff[1]), style=style.studyfluff, xmaximum=450).get_size()[1]
            y += h
            if y>=minheight and y<=maxheight:
                toshow.append(y)
            elif y>maxheight:
                break
        return tuple(toshow)

screen study_fluff_paged:

    vbox xpos 385 ypos 120 at study_fluff_fade:
        for fluffitem in study_fluff_results_between(study_results[2], minheight, maxheight):
            hbox:
                text (str(fluffitem[0]) + ':') style style.studyfluff
                null width 10
                text _(str(fluffitem[1])) style style.studyfluff xmaximum 450

screen study_anim:
    text _(current_activity) style style.studybold pos (303, 426)
    add 'bigbar_left':
        xpos 402
        ypos 471
        crop (0, 0, 4 + int(val * 2.06), 32)
        yanchor 0.5
    text ('%.2f' % val) style style.studybold:
        xpos 382
        ypos 471
        xanchor 1.0
        yanchor 0.5
    text (_('Increased by %.2f') % (val - (study_results[4] - study_results[1]))):
        xpos 636
        ypos 471
        yanchor 0.5
        style style.studybold

init python:
    mood_bonuses = {
        'Afraid':('Faith','Agility'),
        'Angry':('Weapons','Military'),
        'Depressed':('Expression','Animal Handling'),
        'Cheerful':('Athletics','Conversation'),
        'Yielding':('History','Royal Demeanor','Faith'),
        'Willful':('Lumen','Intrigue','Military'),
        'Lonely':('Conversation','Medicine'),
        'Pressured':('Athletics','Faith'),
        'Injured':(),
        'Neutral':(),
        }
    mood_penalties = {
        'Afraid':('Royal Demeanor','Weapons','Military','Intrigue'),
        'Angry':('Royal Demeanor','Medicine','Animal Handling','Expression'),
        'Depressed':('Royal Demeanor','Conversation','Athletics'),
        'Cheerful':('Weapons','Military','Intrigue'),
        'Yielding':('Lumen','Weapons'),
        'Willful':('Royal Demeanor','History','Economics'),
        'Lonely':('Faith','Royal Demeanor','Intrigue'),
        'Pressured':('Conversation','History','Economics'),
        'Injured':('Agility','Weapons','Athletics','Animal Handling'),
        'Neutral':(),
        }

screen bonus_penalty:
    if Stat.instances[current_activity].subgroup.name in mood_penalties[mood]:
        hbox xpos 318 ypos 488:
            add 'heart.png' zoom 0.77
            null width 15
            text (_('Penalty: %s') % _(mood)) style style.studybold yalign 0.5
    elif Stat.instances[current_activity].subgroup.name in mood_bonuses[mood]:
        hbox xpos 318 ypos 488:
            add 'heart.png' zoom 0.77
            null width 15
            text (_('Bonus: %s') % _(mood)) style style.studybold yalign 0.5

init python:
    def study_fluff_size():
        try:
            size = style.studyfluff.size
            while size>10:
                h = 0
                for item in study_results[2]:
                    h += Text(item[1], style=style.studyfluff, xmaximum=450, size=size).render(450,1000,0,0).get_size()[1]
                if h<305:
                    return size
                size -= 1
            return size
        except:
            return 15

label show_activity:

    show screen study_fluff(size=study_fluff_size())


    show bigbar_right:
        xpos 402
        ypos 471
        yanchor .5
    show screen bonus_penalty
    show screen study_anim (val=study_results[4]-study_results[1])
    pause .4
    show screen study_anim (val=study_results[4]-(study_results[1]*.8))
    pause .4
    show screen study_anim (val=study_results[4]-(study_results[1]*.6))
    pause .4
    show screen study_anim (val=study_results[4]-(study_results[1]*.4))
    pause .4
    show screen study_anim (val=study_results[4]-(study_results[1]*.2))
    pause .4
    show screen study_anim (val=study_results[4])
    pause



    if study_results[3]:
        python:
            unlocks = study_results[3]
            can_show_skip = False
        "%(unlocks)s"
        $ can_show_skip = True
    hide screen study_anim
    hide screen study_fluff
    hide screen bonus_penalty
    hide bigbar_right
    return

label start_week:
    python:
        weekday = 0

label do_week:
    call switchfade_studying
    scene statsbg
    show expression PrincessSprite(mood,xanchor=.5) as princess at Position(xpos=.5)
    with dissolve
    show expression PrincessSprite(mood,xanchor=.5) as princess:
        linear 1.0 xpos .165
    show big_ribbonbox_blue behind princess with dissolve:
        xalign .5
        yalign .5
    python:
        new_outfits = 0
        current_activity = current_morning_activity
        timeofday = 'Morning'
        weeknum += 1
        renpy.exports.log = readback_log
        readback_log(_("(Studied %s in the morning.)")%current_morning_activity)
        readback_log('')
        study_results = study(current_morning_activity)
        if sense_magic>=80 and Stat.instances[current_morning_activity].subgroup=='Faith' and ('week34_concert' not in flags):
            flags['can_talk_to_ursul_about_selene'] = True
    show expression Text(_("Week %(weeknum)d - %(timeofday)s")%dict(weeknum=weeknum,timeofday=_(timeofday)),xalign=.5,ypos=81,yanchor=0,style=style.studybold) as week_n_time with dissolve
    pause 0.05
    call show_activity
    python:
        current_activity = current_evening_activity
        readback_log(_("(Studied %s in the afternoon.)")%current_evening_activity)
        readback_log('')
        study_results = study(current_evening_activity)
        timeofday = 'Afternoon'
        if sense_magic>=80 and Stat.instances[current_activity].subgroup=='Faith' and ('week34_concert' not in flags):
            flags['can_talk_to_ursul_about_selene'] = True
    show expression Text(_("Week %(weeknum)d - %(timeofday)s")%dict(weeknum=weeknum,timeofday=_(timeofday)),xalign=.5,ypos=81,yanchor=0,style=style.studybold) as week_n_time with dissolve
    call show_activity
    python:
        readback_log('')
        update_bonuses()
        update_adjusted_stats()
        lassi -= (int(renpy.random.random()*49)+1)*.01
    return

init python:
    def primary_subskill_group():
        high = 0
        candidates = []
        for grp in Subgroup.instances:
            go = Subgroup.instances[grp]
            skilltot = eval(go.stats[0].varname+'+'+go.stats[1].varname+'+'+go.stats[2].varname)
            if skilltot>high:
                candidates = [go]
                high = skilltot
            elif skilltot==high:
                candidates.append(go)
        if len(candidates)>1:
            return renpy.random.choice(candidates).name
        return candidates[0].name
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
