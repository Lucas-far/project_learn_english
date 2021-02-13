

""""""
"------------------------------------------------------- NOMES -------------------------------------------------------"
##

names = [
    'Alice', 'Ana Clara', 'Arthur', 'Beatriz', 'Bernardo', 'Daniel', 'Davi', 'Eduardo', 'Enzo', 'Felipe', 'Gabriel',
    'Gabriela', 'Giovanna', 'Guilherme', 'Gustavo', 'Heitor', 'Helena', 'Heloísa', 'Henrique', 'Isabella', 'Isadora',
    'João Pedro', 'Julia', 'Lara', 'Laura', 'Leonardo', 'Lorena', 'Lorenzo', 'Lucas', 'Luiza', 'Lívia', 'Manuela',
    'Maria Clara', 'Maria Eduarda', 'Maria Luiza', 'Mariana', 'Matheus', 'Miguel', 'Murilo', 'Nicolas', 'Nicole',
    'Pedro', 'Rafael', 'Rafaela', 'Samuel', 'Sophia', 'Theo', 'Valentina', 'Vitor', 'Yasmin'
]

"----------------------------------------------------- VERBO CAN -----------------------------------------------------"
##

can_could_global = [
    'can', "can't", 'cannot', 'could', "couldn't", 'could not'
    'Can', "Can't", 'Cannot', 'Could', "Couldn't", 'Could not'
]

can_l, can_u = ['can'], ['Can']
can_ng_large_l, can_ng_large_u = ['cannot'], ['Cannot']
can_ng_short_l, can_ng_short_u = ["can't"], ["Can't"]

could_l, could_u = ['could'], ['Could']
could_ng_large_l, could_ng_large_u = ['could not'], ['Could not']
could_ng_short_l, could_ng_short_u = ["couldn't"], ["Couldn't"]

can_subject_not = [
    'Can I not', 'Can you not', 'Can he not', 'Can she not', 'Can it not', 'Can we not', 'Can they not'
]

could_subject_not = [
    'Could I not', 'Could you not', 'Could he not', 'Could she not', 'Could it not', 'Could we not', 'Could they not'
]

"--------------------------------------------------- VERBO HAS/HAVE ---------------------------------------------------"

has_have_gl = ['Has', 'Has not', "Hasn't", 'has', 'has not', "hasn't", 'Have', 'Have not', "Haven't", 'have',
               'have not', "haven't"]

has_have_all_u = ['Has', 'Have']
has_have_all_l = ['has', 'have']
the_has_u = ['Has']
the_has_l = ['has']
the_have_u = ['Have']
the_have_l = ['have']

"------------------------------------------------------ ARTIGOS ------------------------------------------------------"
##

art_gl = ['The', 'the', 'A', 'an', ]
art_all_u = ['A', 'An', 'The']
art_all_l = ['a', 'an', 'the']
art_undef_u = ['A', 'An']
art_undef_l = ['a', 'an']
art_the_u = ['The']
art_the_l = ['the']


"------------------------------------------------------ PRONOMES ------------------------------------------------------"
##

pro_gl = [
    'I', 'you', 'he', 'she', 'it', 'we', 'you', 'they',
    'I', 'You', 'He', 'She', 'It', 'We', 'You', 'They'
]

pro_gl_u = ['I', 'You', 'He', 'She', 'It', 'We', 'You', 'They']
pro_gl_l = ['I', 'you', 'he', 'she', 'it', 'we', 'you', 'they']

pro_sgl_u = ['I', 'He', 'She', 'It']
pro_sgl_l = ['I', 'he', 'she', 'it']

pro_sgl_others_u = ['He', 'She', 'It']
pro_sgl_others_l = ['he', 'she', 'it']

pro_pl_u = ['We', 'You', 'They']
pro_pl_l = ['we', 'you', 'they']

pro_pl_others_u = ['I', 'We', 'You', 'They']
pro_pl_others_l = ['I', 'we', 'you', 'they']

i_u, you_u, he_u, she_u, it_u, we_u, they_u = \
    ['I'], ['You'], ['He'], ['She'], ['It'], ['We'], ['They']

i_l, you_l, he_l, she_l, it_l, we_l, they_l = \
    ['I'], ['you'], ['he'], ['she'], ['it'], ['we'], ['they']

"---------------------------------------------------- VERBO TO BE ----------------------------------------------------"
##

to_be_pst_gl = ['am', 'are', 'is', 'Am', 'Are', 'Is']
to_be_pst_all_u = ['Am', 'Are', 'Is']
to_be_pst_all_l = ['am', 'are', 'is']

to_be_pst_sgl_u = ['Am', 'Is']
to_be_pst_sgl_l = ['am', 'is']

are_u = ['Are']
are_l = ['are']

am_l = ['am']
am_u = ['Am']

is_l = ['is']
is_u = ['Is']

"--------------------------------------------------- VERBO AUXILIAR ---------------------------------------------------"
##

do_does_gl = ['Do', 'Does', 'do', 'does']

the_do_u = ['Do']
the_do_l = ['do']

the_does_u = ['Does']
the_does_l = ['does']

"---------------------------------------------------- SEPARADORES ----------------------------------------------------"
##

and_ = ['and']

"---------------------------------------------- PRONOMES DEMONSTRATIVOS ----------------------------------------------"
##

l_this, l_that, l_these, l_those = ['this'], ['that'], ['these'], ['those']
u_this, u_that, u_these, u_those = ['This'], ['That'], ['These'], ['Those']

demo_sgl_l = ['this', 'that']
demo_sgl_u = ['This', 'That']

demo_pl_l = ['these', 'those']
demo_pl_u = ['These', 'Those']

demo_all_l = ['this', 'these', 'that', 'those']
demo_all_u = ['This', 'These', 'That', 'Those']

# pronouns_demonstrative = [*pronouns_demonstrative_lower, *pronouns_demonstrative_upper]
demo_gl = ['this', 'these', 'that', 'those', 'This', 'These', 'That', 'Those']

"----------------------------------------------- ADJETIVOS POSSESSIVOS -----------------------------------------------"
##

adj_pos_l = ['my', 'your', 'his', 'her', 'its', 'our', 'their']
# adjectives_possessive_upper = [index.replace(index[0], index[0].upper()) for index in adjectives_possessive_lower]
adj_pos_u = ['My', 'Your', 'His', 'Her', 'Its', 'Our', 'Their']

"--------------------------------------------------- SUBSTANTIVOS ---------------------------------------------------"
##

nouns = [
    'air', 'airs', 'area', 'areas', 'art', 'arts', 'bodies', 'body', 'book', 'books', 'business', 'businesses', 'car',
    'cars', 'case', 'cases', 'change', 'changes', 'child', 'children',

    'cities', 'city', 'communities', 'community', 'companies', 'company', 'countries', 'country', 'day', 'days', 'door',
    'doors', 'ending', 'endings', 'eye', 'eyes', 'face', 'faces', 'fact', 'facts',

    'families', 'family', 'father', 'fathers', 'force', 'forces', 'friend', 'friends', 'game', 'games', 'girl', 'girls',
    'government', 'governments', 'group', 'groups', 'guy', 'guys', 'hand', 'hands',

    'head', 'heads', 'histories', 'history', 'home', 'homes', 'hour', 'hours', 'house', 'houses', 'idea', 'ideas',
    'issue', 'issues', 'job', 'jobs', 'kid', 'kids', 'kind', 'kinds',

    'law', 'laws', 'level', 'levels', 'life', 'lifes', 'line', 'lines', 'lot', 'lots', 'man', 'member', 'members',
    'men', 'minute', 'minutes', 'moment', 'moments', 'month', 'months',

    'morning', 'mornings', 'mother', 'mothers', 'name', 'names', 'night', 'nights', 'number', 'numbers', 'office',
    'offices', 'other', 'others', 'parent', 'parents', 'part', 'parties', 'parts', 'party',

    'person', 'person', 'piece of information', 'pieces of information', 'place', 'places', 'point',
    'points', 'power', 'powers', 'president', 'presidents', 'problem', 'problems', 'program', 'programs', 'question',
    'questions',

    'reason', 'reasons', 'research', 'researches', 'result', 'results', 'right', 'rights', 'room', 'rooms', 'school',
    'schools', 'service', 'services', 'side', 'sides', 'state', 'states', 'stories', 'story',

    'student', 'students', 'studies', 'study', 'system', 'systems', 'teacher', 'teachers', 'team', 'teams', 'thing',
    'things', 'time', 'times', 'war', 'wars', 'water', 'waters', 'way', 'ways',

    'week', 'weeks', 'woman', 'women', 'word', 'words', 'work', 'works', 'world', 'worlds', 'year', 'years'
]
# print('nouns = ', len(nouns))

# nouns_singular = []
# box = [nouns_singular.append(index) for index in nouns if index[-1] != 's']
# print(nouns_singular)

nouns_sgl = [
    'air', 'area', 'art', 'body', 'book', 'business', 'car', 'case', 'change', 'city', 'child', 'community',
    'company', 'country', 'day', 'door', 'ending', 'eye', 'face', 'fact',

    'family', 'father', 'force', 'friend', 'game', 'girl', 'government', 'group', 'guy', 'hand', 'head', 'history',
    'home', 'hour', 'house', 'idea', 'issue', 'job', 'kid', 'kind',

    'law', 'level', 'life', 'line', 'lot', 'man', 'member', 'minute', 'moment', 'month', 'morning', 'mother',
    'name', 'night', 'number', 'office', 'other', 'parent', 'part',

    'party', 'person', 'place', 'point', 'piece of information', 'power', 'president', 'problem', 'program', 'question',
    'reason', 'research', 'result', 'right', 'room', 'school',

    'service', 'side', 'state', 'story', 'student', 'study', 'system', 'teacher', 'team', 'thing', 'time', 'war',
    'water', 'way', 'week', 'woman', 'word', 'work', 'world',

    'year',
]
# print('nouns_singular = ', len(nouns_singular))

nouns_pl = [
    'airs', 'areas', 'arts', 'bodies', 'books', 'businesses', 'cars', 'cases', 'changes', 'cities', 'children',
    'communities', 'companies', 'countries', 'days', 'doors', 'endings', 'eyes', 'faces', 'facts',

    'families', 'fathers', 'forces', 'friends', 'games', 'girls', 'governments', 'groups', 'guys', 'hands', 'heads',
    'histories', 'homes', 'hours', 'houses', 'ideas', 'issues', 'jobs', 'kids', 'kinds',

    'laws', 'levels', 'lifes', 'lines', 'lots', 'men', 'members', 'minutes', 'moments', 'months', 'mornings', 'mothers',
    'names', 'nights', 'numbers', 'offices', 'others', 'parents', 'parts',

    'parties', 'people', 'places', 'points', 'pieces of information', 'powers', 'presidents', 'problems', 'programs',
    'questions', 'reasons', 'researches', 'results', 'rights', 'rooms', 'schools',

    'services', 'sides', 'states', 'stories', 'students', 'studies', 'systems', 'teachers', 'teams', 'things', 'times',
    'wars', 'waters', 'ways', 'weeks', 'women', 'words', 'works', 'worlds',

    'years']
# box2 = [nouns_plural.append(index) for index in nouns if index[-1] == 's']
# print(nouns_plural)
# print('nouns_plural = ', len(nouns_plural))

"IMPORTANTE PARA COMPARAÇÃO"
# for x in zip(nouns_singular, nouns_plural):
#     print(x)

"----------------------------------------------------- ADVÉRBIOS -----------------------------------------------------"
##

adv_gl = [
    'about', 'accidentally', 'actually', 'again', 'ago', 'ahead', 'all', 'almost', 'alone', 'already', 'also', 'always',
    'angrily', 'anxiously', 'around', 'as', 'away', 'awkwardly', 'back', 'badly',

    'before', 'best', 'better', 'blindly', 'boastfully', 'boldly', 'both', 'bravely', 'brightly', 'certainly',
    'cheerfully', 'clearly', 'close', 'coyly', 'crazily', 'defiantly', 'deftly', 'deliberately', 'devotedly',
    'directly',

    'doubtfully', 'down', 'dramatically', 'dutifully', 'eagerly', 'early', 'either', 'elegantly', 'else', 'enormously',
    'enough', 'especially', 'even', 'evenly', 'eventually', 'ever', 'exactly', 'faithfully', 'far', 'fast',

    'finally', 'foolishly', 'fortunately', 'forward', 'frequently', 'gleefully', 'gracefully', 'happily', 'hard',
    'hastily', 'here', 'honestly', 'hopelessly', 'hourly', 'how', 'however', 'hungrily', 'in', 'indeed', 'innocently',

    'inquisitively', 'instead', 'irritably', 'jealously', 'just', 'justly', 'kindly', 'later', 'lazily', 'least',
    'less', 'little', 'long', 'loosely', 'madly', 'maybe', 'merrily', 'more', 'mortally', 'most',

    'much', 'mysteriously', 'nearly', 'nervously', 'never', 'no', 'normally', 'now', 'obediently', 'obnoxiously',
    'occasionally', 'of course', 'off', 'often', 'ok', 'on', 'once', 'only', 'out', 'over',

    'particularly', 'perfectly', 'perhaps', 'politely', 'poorly', 'powerfully', 'pretty', 'probably', 'promptly',
    'quickly', 'quite', 'rapidly', 'rarely', 'rather', 'really', 'recently', 'regularly', 'right', 'rudely', 'safely',

    'seldom', 'selfishly', 'seriously', 'shakily', 'sharply', 'silently', 'simply', 'slowly', 'so', 'solemnly',
    'sometimes', 'soon', 'speedily', 'sternly', 'still', 'suddenly', 'technically', 'tediously', 'that', 'then',

    'there', 'thus', 'to', 'today', 'together', 'tonight', 'unexpectedly', 'up', 'usually', 'very', 'victoriously',
    'vivaciously', 'warmly', 'wearily', 'weekly', 'well', 'when', 'where', 'why', 'wildly',

    'yearly', 'yet'
]

# print(adverbs_ly := [index for index in adverbs if index[-1] == 'y' and index[-2] == 'l'])
adv_ly = [
    'actually', 'already', 'certainly', 'clearly', 'directly', 'early', 'especially', 'eventually', 'exactly',
    'finally', 'nearly', 'normally', 'only', 'particularly', 'probably', 'quickly', 'recently', 'simply', 'suddenly',
    'usually', 'accidentally', 'awkwardly', 'blindly', 'coyly', 'crazily', 'defiantly', 'deliberately', 'doubtfully',
    'dramatically', 'dutifully', 'enormously', 'evenly', 'hastily', 'hungrily', 'inquisitively', 'loosely',
    'madly', 'mortally', 'mysteriously', 'nervously', 'seriously', 'shakily', 'sharply', 'silently', 'solemnly',
    'sternly', 'technically', 'unexpectedly', 'wildly'
]

adv_frequency = [
    'always', 'eventually', 'finally', 'frequently', 'hourly', 'never', 'occasionally', 'often', 'rarely', 'regularly',
    'seldom', 'sometimes', 'usually', 'weekly', 'yearly'
]

adv_action = ['promptly', 'quickly', 'rapidly', 'slowly', 'speedily', 'tediously']

adv_negativity = [
    'angrily', 'anxiously', 'badly', 'boastfully', 'foolishly', 'hopelessly', 'irritably', 'jealously', 'lazily',
    'obnoxiously', 'poorly', 'rudely', 'selfishly', 'wearily'
]

adv_positivity = [
    'boldly', 'bravely', 'brightly', 'cheerfully', 'deftly', 'devotedly', 'eagerly', 'elegantly', 'faithfully',
    'fortunately', 'gleefully', 'gracefully', 'happily', 'honestly', 'innocently', 'justly', 'kindly', 'merrily',
    'obediently', 'perfectly', 'politely', 'powerfully', 'safely', 'victoriously', 'vivaciously', 'warmly'
]

# print(sum([len(adverbs_ly), len(adverbs_time), len(adverbs_action), len(adverbs_negativity), len(adverbs_positivity)]))
# print(len(adverbs))
# adverbs_ = [*adverbs, *adverbs_ly, *adverbs_time, *adverbs_action, *adverbs_negativity, *adverbs_positivity]
# print(adverbs_)
# print(len(adverbs_))
# adverbs_ = set(adverbs_)
# print(sorted(adverbs_))
# print(len(adverbs_))

"----------------------------------------------- VERBOS NO INFINITIVO -----------------------------------------------"
##

verbs_inf = [
    'to be', 'to have', 'to do', 'to say', 'to go', 'to get', 'to make', 'to know', 'to think', 'to take',
    'to see', 'to come', 'to want', 'to look', 'to use', 'to find', 'to give', 'to tell', 'to work', 'to call',

    'to try', 'to ask', 'to need', 'to feel', 'to become', 'to leave', 'to put', 'to mean', 'to keep', 'to let',
    'to begin', 'to seem', 'to help', 'to talk', 'to turn', 'to start', 'to show', 'to hear', 'to play', 'to run',

    'to move', 'to like', 'to live', 'to believe', 'to hold', 'to bring', 'to happen', 'to write', 'to provide',
    'to sit', 'to stand', 'to lose', 'to pay', 'to meet', 'to include', 'to continue', 'to set', 'to learn',
    'to change', 'to lead',

    'to understand', 'to watch', 'to follow', 'to stop', 'to create', 'to speak', 'to read', 'to allow', 'to add',
    'to spend', 'to grow', 'to open', 'to walk', 'to win', 'to offer', 'to remember', 'to love', 'to consider',
    'to appear', 'to buy',

    'to wait', 'to serve', 'to die', 'to send', 'to expect', 'to build', 'to stay', 'to fall', 'to cut', 'to reach',
    'to kill', 'to remain', 'to suggest', 'to raise', 'to pass', 'to sell', 'to require', 'to report', 'to decide',
    'to pull',

    'to break', 'to acquire', 'to realize', 'to manage', 'to develop', 'to trust', 'to imagine', 'to step', 'to regret',
    'to manipulate', 'to dream', 'to discuss', 'to drink', 'to eat', 'to skip', 'to see', 'to repeat', 'to know',
    'to guess', 'to select',

    'to click',
]

# print('verbs_infinitive = ', verbs_infinitive)
# print('verbs_infinitive = ', len(verbs_infinitive))
# verbs_present = [x.replace(x, x[3:])for x in verbs_infinitive]
# print('verbs_present = ', verbs_present)
# print('verbs_present = ', len(verbs_present))

"------------------------------------------ VERBOS NO PRESENTE PARA PLURAL ------------------------------------------"
##

pst_pl = [
    'are', 'have', 'do', 'say', 'go', 'get', 'make', 'know', 'think', 'take', 'see', 'come', 'want', 'look', 'use',
    'find', 'give', 'tell', 'work', 'call',

    'try', 'ask', 'need', 'feel', 'become', 'leave', 'put', 'mean', 'keep', 'let', 'begin', 'seem', 'help', 'talk',
    'turn', 'start', 'show', 'hear', 'play', 'run',

    'move', 'like', 'live', 'believe', 'hold', 'bring', 'happen', 'write', 'provide', 'sit', 'stand', 'lose', 'pay',
    'meet', 'include', 'continue', 'set', 'learn', 'change', 'lead',

    'understand', 'watch', 'follow', 'stop', 'create', 'speak', 'read', 'allow', 'add', 'spend', 'grow', 'open', 'walk',
    'win', 'offer', 'remember', 'love', 'consider', 'appear', 'buy',

    'wait', 'serve', 'die', 'send', 'expect', 'build', 'stay', 'fall', 'cut', 'reach', 'kill', 'remain', 'suggest',
    'raise', 'pass', 'sell', 'require', 'report', 'decide', 'pull',

    'break', 'acquire', 'realize', 'manage', 'develop',
    'trust', 'imagine', 'step', 'regret', 'manipulate', 'dream', 'discuss', 'drink', 'eat', 'skip', 'see', 'repeat',
    'know', 'guess', 'select',

    'click'
]
# print('verbs_present_plural = ', len(present_time_tense_plural))
# verbs_present_singular = [x.replace(x, x + 's') for x in verbs_present_plural]
# print(verbs_present_singular)

"----------------------------------------- VERBOS NO PRESENTE PARA SINGULAR -----------------------------------------"
##

pst_sgl = [
    'is', 'has', 'does', 'says', 'goes', 'gets', 'makes', 'knows', 'thinks', 'takes', 'sees', 'comes', 'wants',
    'looks', 'uses', 'finds', 'gives', 'tells', 'works', 'calls',

    'tries', 'asks', 'needs', 'feels', 'becomes', 'leaves', 'puts', 'means', 'keeps', 'lets', 'begins', 'seems', 'helps',
    'talks', 'turns', 'starts', 'shows', 'hears', 'plays', 'runs',

    'moves', 'likes', 'lives', 'believes', 'holds', 'brings', 'happens', 'writes', 'provides', 'sits', 'stands',
    'loses', 'pays', 'meets', 'includes', 'continues', 'sets', 'learns', 'changes', 'leads',

    'understands', 'watches', 'follows', 'stops', 'creates', 'speaks', 'reads', 'allows', 'adds', 'spends', 'grows',
    'opens', 'walks', 'wins', 'offers', 'remembers', 'loves', 'considers', 'appears', 'buys',

    'waits', 'serves', 'dies', 'sends', 'expects', 'builds', 'stays', 'falls', 'cuts', 'reaches', 'kills', 'remains',
    'suggests', 'raises', 'passes', 'sells', 'requires', 'reports', 'decides', 'pulls',

    'breaks', 'acquires', 'realizes', 'manages', 'develops', 'trusts', 'imagines', 'steps', 'regrets', 'manipulates',
    'dreams', 'discusses', 'drinks', 'eats', 'skips', 'sees', 'repeats', 'knows', 'guesses', 'selects',

    'clicks'
]
# print('present_time_tense = ', len(present_time_tense_singular))

"-------------------------------------------- VERBOS NO PASSADO SIMPLES --------------------------------------------"
##

past = [
    'was', 'were', 'had', 'did', 'said', 'went', 'got', 'made', 'knew', 'thought', 'took',
    'saw', 'came', 'wanted', 'looked', 'used', 'found', 'gave', 'told', 'worked',

    'called', 'tried', 'asked', 'needed', 'felt', 'became', 'left', 'put', 'meant', 'kept', 'let',
    'began', 'seemed', 'helped', 'talked', 'turned', 'started', 'showed', 'heard', 'played',

    'ran', 'moved', 'liked', 'lived', 'believed', 'held', 'brought', 'happened', 'wrote', 'provided',
    'sat', 'stood', 'lost', 'paid', 'met', 'included', 'continued', 'set', 'learned', 'changed',

    'led', 'understood', 'watched', 'followed', 'stopped', 'created', 'spoke', 'read',
    'allowed', 'added', 'spent', 'grew', 'opened', 'walked', 'won', 'offered', 'remembered',
    'loved', 'considered', 'appeared',

    'bought', 'waited', 'served', 'died', 'sent', 'expected', 'built', 'stayed', 'fell', 'cut', 'reached', 'killed',
    'remained', 'suggested', 'rose', 'passed', 'sold', 'required', 'reported', 'decided',

    'pulled', 'broke', 'acquired', 'realized', 'managed', 'developed', 'trusted', 'imagined', 'stepped', 'regreted',
    'manipulated', 'dreamed', 'discussed', 'drank', 'ate', 'skept', 'saw', 'repeated', 'knew', 'guessed',

    'selected', 'clicked',
]
# print('past_time_tense = ', len(past_time_tense))

"----------------------------------------------------- ADJETIVOS -----------------------------------------------------"
##

adj = [
    'other', 'new', 'good', 'high', 'old', 'great', 'big', 'American', 'small', 'large', 'national', 'young',
    'different', 'black', 'long', 'little', 'important', 'political', 'bad', 'white',

    'real', 'best', 'right', 'social', 'only', 'public', 'sure', 'low', 'early', 'able', 'human', 'local', 'late',
    'hard', 'major', 'better', 'economic', 'strong', 'possible', 'whole',

    'free', 'military', 'true', 'federal', 'international', 'full', 'special', 'easy', 'clear', 'recent', 'certain',
    'personal', 'open', 'red', 'difficult', 'available', 'likely', 'short', 'single', 'medical',

    'current', 'wrong', 'private', 'past', 'foreign', 'fine', 'common', 'poor', 'natural', 'significant',
    'similar', 'hot', 'dead', 'central', 'happy', 'serious', 'ready', 'simple', 'left', 'physical',

    'general', 'environmental', 'financial', 'blue', 'democratic', 'dark', 'various', 'entire', 'close', 'legal',
    'religious', 'cold', 'final', 'main', 'green', 'nice', 'huge', 'popular', 'traditional', 'cultural',

    'stupid', 'irrelevant', 'sweet', 'angry', 'ambitious', 'indifferent', 'marvelous', 'identical', 'clever',
    'enthusiastic', 'vibrant', 'affirmative', 'negative', 'comprehensive', 'intuitive', 'strange', 'weird', 'odd',
    'worthy', 'flexible'
]

"--------------------------------------------------- PREPOSIÇÕES ---------------------------------------------------"
##

prep = [
    'about', 'above', 'across', 'after', 'against', 'ago', 'among', 'around', 'as', 'at', 'before', 'behind',
    'below', 'between', 'by', 'down', 'during', 'for', 'from', 'in', 'in front of', 'into', 'like', 'of', 'on', 'out',
    'over', 'since', 'through', 'to', 'towards', 'under', 'until', 'up', 'with', 'without'
]

prep_time_l = ['on', 'ago', 'at', 'before', 'by', 'for', 'from', 'in', 'since', 'to', 'until']
prep_time_u = ['On', 'Ago', 'At', 'Before', 'By', 'For', 'From', 'In', 'Since', 'To', 'Until']

prep_direction_place_l = [
    'above', 'across', 'among', 'at', 'behind', 'below', 'between', 'by', 'down', 'from', 'in', 'in front of', 'on',
    'over', 'through', 'to', 'towards', 'under', 'up'
]

# prepositions_direction_place_upper = [index.replace(index, index[0].upper() + index[1:]) for index in prepositions_direction_place_lower]
prep_direction_place_u = [
    'Above', 'Across', 'Among', 'At', 'Behind', 'Below', 'Between', 'By', 'Down', 'From', 'In', 'In front of', 'On',
    'Over', 'Through', 'To', 'Towards', 'Under', 'Up']

prep_agent = ['about', 'by', 'for', 'of', 'with']

prep_phrasal_l = [
    'according to', 'along with', 'apart from', 'because of', 'by means of', 'contrary to', 'in addition to',
    'in front of', 'in reference to', 'in regard to', 'in spite of', 'instead of', 'on account of', 'on top of',
    'out of', 'with regard to'
]

# preposititons_phrasal_upper = [index.replace(index, index[0].upper() + index[1:]) for index in preposititons_phrasal_lower]
prep_phrasal_u = [
    'According to', 'Along with', 'Apart from', 'Because of', 'By means of', 'Contrary to', 'In addition to',
    'In front of', 'In reference to', 'In regard to', 'In spite of', 'Instead of', 'On account of', 'On top of',
    'Out of', 'With regard to'
]

"------------------------------------------------- PRONOMES OBJETO -------------------------------------------------"
##

pro_obj = ['me', 'you', 'him', 'her', 'it', 'us', 'them']

"----------------------------------------------- PRONOMES POSSESSIVOS -----------------------------------------------"
##

pro_pos = ['mine', 'yours', 'his', 'hers', 'its', 'ours', 'theirs']

"-------------------------------------------------------- WILL --------------------------------------------------------"
##

will_u = ['Will']
will_l = ['will']
will_ng_long_u = ['Will not']
will_ng_long_l = ['will not']
will_ng_short_u = ["Won't"]
will_ng_short_l = ["won't"]

will_subject_not = [
    'Will I not', 'Will you not', 'Will he not', 'Will she not', 'Will it not', 'Will we not', 'Will they not'
]

# When to use [ will ]
def obs_will():
    """
    - beliefs, willingness, promises, offers, requests, conditions about the present or future

    EXAMPLES:
        -> They will find the place [ willingness ]
        -> I will help you [ promises ]
        -> He will give one of his clothings [ offers ]
        -> We will require your attention [ requests ]
        -> She will call her if she can find her number [ conditions ]
    """

"------------------------------------------------------- WOULD -------------------------------------------------------"
##

would_g = ['Would', 'would']
would_u = ['Would']
would_l = ['would']

# When to use [ would ]
def obs_would():
    """
    - it is the past tense form of will. Because it is a past tense, it is used:
    - to talk about the past, hypotheses, politeness

     EXAMPLES:
        -> I would take the bus, if I were fast enough [ past ]
        -> He would eat pizza at night, because he is addicted [ hypotheses ]
        -> Would you sit, please? [ politeness ]
    """

"----------------------------------------------------- PERGUNTAS -----------------------------------------------------"

wh_gl = [
    'How', 'What', 'When', 'Where', 'Which', 'Who', 'Whose', 'Why',
    'how', 'what', 'when', 'where', 'which', 'who', 'whose', 'why'
]

wh_all_u = ['How', 'What', 'When', 'Where', 'Which', 'Who', 'Whose', 'Why']
wh_all_l = ['how', 'what', 'when', 'where', 'which', 'who', 'whose', 'why']

wh_specific_u = ['How', 'Where', 'Who']
wh_specific_l = ['how', 'where', 'who']

if __name__ == '__main__':
    # print('nouns = ', len(nouns))
    # print('nouns_singular = ', len(nouns_singular))
    # print('nouns_plural = ', len(nouns_plural))
    # print('verbs_infinitive = ', len(verbs_infinitive))
    # print('verbs_present_plural = ', len(present_time_tense_plural))
    # print('present_time_tense = ', len(present_time_tense_singular))
    # print('past_time_tense = ', len(past_time_tense))
    # print(sorted(wh))
    pass
