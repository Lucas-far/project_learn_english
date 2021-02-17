

pst_pl_dict = {
    'say': ('say', 'dizem/falam'),
    'go': ('go', 'vão'),
    'get': ('get', 'adquirem/conseguem/obtem/pegam'),
    'make': ('make', 'criam/fazem'),
    'know': ('know', 'conhecem/sabem'),
    'think': ('think', 'acham/pensam'),
    'take': ('take', 'levam/pegam/tomam'),
    'see': ('see', 'vêem'),
    'come': ('come', 'chegam/vêm'),
    'want': ('want', 'pretendem/querem'),
    'look': ('look', 'olham/vêem'),
    'use': ('use', 'usam'),
    'find': ('find', 'acham/encontram'),
    'give': ('give', 'dão'),
    'tell': ('tell', 'contam/dizem'),
    'work': ('work', 'funcionam/trabalham'),
    'call': ('call', 'chamam/telefonam'),
    'try': ('try', 'experimentam/tentam'),
    'ask': ('ask', 'pedem/perguntam'),
    'need': ('need', 'necessitam/precisam'),
    'feel': ('feel', 'sentem'),
    'become': ('become', 'tornam-se'),
    'leave': ('leave', 'abandonam/deixam/saem'),
    'put': ('put', 'colocam/põem'),
    'mean': ('mean', 'significam'),
    'keep': ('keep', 'continuam/guardam/mantêm'),
    'let': ('let', 'deixam/permitem'),
    'begin': ('begin', 'começam/iniciam'),
    'seem': ('seem', 'parecem'),
    'help': ('help', 'ajudam/auxiliam'),
    'talk': ('talk', 'conversam/falam'),
    'turn': ('turn', 'transformam/viram'),
    'start': ('start', 'começam/iniciam'),
    'show': ('show', 'apresentam/mostram'),
    'hear': ('hear', 'escutam/ouvem'),
    'play': ('play', 'jogam/tocam'),
    'run': ('run', 'correm'),
    'move': ('move', 'movem/mexem'),
    'like': ('like', 'gostam'),
    'live': ('live', 'moram/vivem'),
    'believe': ('believe', 'acreditam/crêem'),
    'hold': ('hold', 'mantêm/seguram'),
    'bring': ('bring', 'trazem'),
    'happen': ('happen', 'acontecem/ocorrem'),
    'write': ('write', 'escrevem'),
    'provide': ('provide', 'fornecem/proporcionam'),
    'sit': ('sit', 'sentam'),
    'stand': ('stand', 'levantam/permanecem'),
    'lose': ('lose', 'perdem'),
    'pay': ('pay', 'pagam'),
    'meet': ('meet', 'conhecem/encontram'),
    'include': ('include', 'incluem'),
    'continue': ('continue', 'continuam'),
    'set': ('set', 'configuram/definem/estabelecem/põem'),
    'learn': ('learn', 'aprendem'),
    'change': ('change', 'alteram/mudam'),
    'lead': ('lead', 'conduzem/lideram'),
    'understand': ('understand', 'compreendem/entendem'),
    'watch': ('watch', 'olham/observam/vêem'),
    'follow': ('follow', 'acompanham/seguem'),
    'stop': ('stop', 'impedem/param'),
    'create': ('create', 'criam'),
    'speak': ('speak', 'conversam/falam'),
    'read': ('read', 'lêem'),
    'allow': ('allow', 'autorizam/permitem'),
    'add': ('add', 'acrescentam/adicionam'),
    'spend': ('spend', 'gastam/passam'),
    'grow': ('grow', 'aumentam/crescem'),
    'open': ('open', 'abrem'),
    'walk': ('walk', 'andam/caminham'),
    'win': ('win', 'ganham/vencem'),
    'offer': ('offer', 'oferecem/propõem'),
    'remember': ('remember', 'lembram/recordam'),
    'love': ('love', 'adoram/amam'),
    'consider': ('consider', 'consideram'),
    'appear': ('appear', 'aparecem'),
    'buy': ('buy', 'compram'),
    'wait': ('wait', 'esperam'),
    'serve': ('serve', 'servem'),
    'die': ('die', 'falecem/morrem'),
    'send': ('send', 'enviam/mandam'),
    'expect': ('expect', 'esperam'),
    'build': ('build', 'constroem'),
    'stay': ('stay', 'ficam/permanecem'),
    'fall': ('fall', 'caem'),
    'cut': ('cut', 'cortam'),
    'reache': ('reache', 'alcançam/atingem/chegam'),
    'kill': ('kill', 'matam'),
    'remain': ('remain', 'ficam/permanecem'),
    'suggest': ('suggest', 'sugerem'),
    'raise': ('raise', 'aumentam/criam alguém,algo/levantam'),
    'pass': ('pass', 'passam'),
    'sell': ('sell', 'vendem'),
    'require': ('require', 'exigem/necessitam'),
    'report': ('report', 'relatam/reportam'),
    'decide': ('decide', 'decidem'),
    'pull': ('pull', 'puxam'),
    'break': ('break', 'rompem/quebram'),
    'acquire': ('acquire', 'adquirem/compram/obtém'),
    'realize': ('realize', 'percebem/realizam'),
    'manage': ('manage', 'administram/gerem'),
    'develop': ('develop', 'crescem/desenvolvem'),
    'trust': ('trust', 'confiam'),
    'imagine': ('imagine', 'imaginam'),
    'step': ('step', 'pisam'),
    'regret': ('regret', 'arrependem/lamentam'),
    'manipulate': ('manipulate', 'manipulam'),
    'dream': ('dream', 'sonham'),
    'discuss': ('discuss', 'debatem/discutem'),
    'drink': ('drink', 'bebem'),
    'eat': ('eat', 'comem'),
    'skip': ('skip', 'pulam/saltam'),
    'repeat': ('repeat', 'repetem'),
    'guess': ('guess', 'adivinham/supõem'),
    'select': ('select', 'selecionam'),
    'click': ('click', 'clicam'),
}

pst_pl_dict_keys = [word for word in pst_pl_dict]

pst_pl_dict_values = [word[1] for word in pst_pl_dict.values()]

pst_pl_dict_uniques = {
    'are': ('are', 'são/estão/ficam'),
    'have': ('have', 'têm'),
    'do': ('do', 'fazem')
}

pst_pl = [
    'say', 'go', 'get', 'make', 'know', 'think', 'take', 'see', 'come', 'want', 'look', 'use',
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



# values = [word[1] for word in pst_sgl_dict.values()]

if __name__ == '__main__':
    pass
    print(len(pst_pl_dict))
    # print(values)
    # print(len(pst_pl))
    # counter = 0
    # while counter < len(pst_sgl_dict):
    #     # print(f"{verbs_inf[counter]}_ = ['{verbs_inf[counter]}', '{verbs_inf_pt_br[counter]}']")
    #     print(f"'{verbs_inf[counter]}': ('{verbs_inf[counter]}', '{verbs_inf_pt_br[counter]}'),")
    #     counter += 1