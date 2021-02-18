

past_dict = {
    'said': ('said', 'disse/falei'),
    'went': ('went', 'fui'),
    'got': ('got', 'adquiri/consegui/obtive/peguei'),
    'made': ('made', 'criei/fiz'),
    'knew': ('knew', 'conheci/sabia'),
    'thought': ('thought', 'achei/pensei'),
    'took': ('took', 'levei/peguei/tomei'),
    'saw': ('saw', 'vi'),
    'came': ('came', 'cheguei/vim'),
    'wanted': ('wanted', 'pretendia/queria'),
    'looked': ('looked', 'olhei/vi'),
    'used': ('used', 'usei'),
    'found': ('found', 'achei/encontrei'),
    'gave': ('gave', 'dei'),
    'told': ('told', 'contei/disse'),
    'worked': ('worked', 'funcionei/trabalhei'),
    'called': ('called', 'chamei/telefonei'),
    'tried': ('tried', 'experimentei/tentei'),
    'asked': ('asked', 'pedi/perguntei'),
    'needed': ('needed', 'necessitei/precisei'),
    'felt': ('felt', 'senti'),
    'became': ('became', 'me tornei'),
    'left': ('left', 'abandonei/deixei/sai'),
    'put': ('put', 'coloquei/pus'),
    'meant': ('meant', 'signifiquei'),
    'kept': ('kept', 'continuei/guardei/mantive'),
    'let': ('let', 'deixei/permiti'),
    'began': ('began', 'começei/iniciei'),
    'seemed': ('seemed', 'pareci'),
    'helped': ('helped', 'ajudei/auxiliei'),
    'talked': ('talked', 'conversei/falei'),
    'turned': ('turned', 'transformei/virei'),
    'started': ('started', 'começei/iniciei'),
    'showed': ('showed', 'apresentei/mostrei'),
    'heard': ('heard', 'escutei/ouvi'),
    'played': ('played', 'joguei/toquei'),
    'ran': ('ran', 'corri'),
    'moved': ('moved', 'movi/mexi'),
    'liked': ('liked', 'gostei'),
    'lived': ('lived', 'morei/vivi'),
    'believed': ('believed', 'acreditei/cri'),
    'held': ('held', 'mantive/segurei'),
    'brought': ('brought', 'trouxe'),
    'happened': ('happened', 'aconteci/ocorri'),
    'wrote': ('wrote', 'escrevi'),
    'provided': ('provided', 'forneci/proporcionei'),
    'sat': ('sat', 'sentei'),
    'stood': ('stood', 'levantei/permaneci'),
    'lost': ('lost', 'perdi'),
    'paid': ('paid', 'paguei'),
    'met': ('met', 'conheci/encontrei/reuni'),
    'included': ('included', 'inclui'),
    'continued': ('continued', 'continuei'),
    'set': ('set', 'configurei/defini/estabeleci/pus'),
    'learned': ('learned', 'aprendi'),
    'changed': ('changed', 'alterei/mudei'),
    'led': ('led', 'conduzi/liderei'),
    'understood': ('understood', 'compreendi/entendi'),
    'watched': ('watched', 'olhei/observei/vi'),
    'followed': ('followed', 'acompanhei/segui'),
    'stopped': ('stopped', 'impedi/parei'),
    'created': ('created', 'criei'),
    'spoke': ('spoke', 'conversei/falei'),
    'read': ('read', 'li'),
    'allowed': ('allowed', 'autorizei/permiti'),
    'added': ('added', 'acrescentei/adicionei'),
    'spent': ('spent', 'gastei/passei'),
    'grew': ('grew', 'aumentei/cresci'),
    'opened': ('opened', 'abri'),
    'walked': ('walked', 'andei/caminhei'),
    'won': ('won', 'ganhei/venci'),
    'offered': ('offered', 'ofereci/propus'),
    'remembered': ('remembered', 'lembrei/recordei'),
    'loved': ('loved', 'adorei/amei'),
    'considered': ('considered', 'considerei'),
    'appeared': ('appeared', 'apareci'),
    'bought': ('bought', 'comprei'),
    'waited': ('waited', 'esperei'),
    'served': ('served', 'servi'),
    'died': ('died', 'faleci/morri'),
    'sent': ('sent', 'enviei/mandei'),
    'expected': ('expected', 'esperei'),
    'built': ('built', 'construi'),
    'stayed': ('stayed', 'fiquei/permaneci'),
    'fell': ('fell', 'cai'),
    'cut': ('cut', 'cortei'),
    'reached': ('reached', 'alcançei/atingi/cheguei a'),
    'killed': ('killed', 'matei'),
    'remained': ('remained', 'fiquei/permaneci'),
    'suggested': ('suggested', 'sugeri'),
    'rose': ('rose', 'aumentei/criei alguém,algo/levantei'),
    'passed': ('passed', 'passei'),
    'sold': ('sold', 'vendi'),
    'required': ('required', 'exigi/necessitei'),
    'reported': ('reported', 'relatei/reportei'),
    'decided': ('decided', 'decidi'),
    'pulled': ('pulled', 'puxei'),
    'broke': ('broke', 'rompi/quebrei'),
    'acquired': ('acquired', 'adquiri/comprei/obtive'),
    'realized': ('realized', 'percebi/realizei'),
    'managed': ('managed', 'administrei/geri'),
    'developed': ('developed', 'cresci/desenvolvi'),
    'trusted': ('trusted', 'confiei'),
    'imagined': ('imagined', 'imaginei'),
    'stepped': ('stepped', 'pisei'),
    'regreted': ('regreted', 'arrependi/lamentei'),
    'manipulated': ('manipulated', 'manipulei'),
    'dreamed': ('dreamed', 'sonhei'),
    'discussed': ('discussed', 'debati/discuti'),
    'drank': ('drank', 'bebi'),
    'ate': ('ate', 'comi'),
    'skept': ('skept', 'pulei/saltei'),
    'repeated': ('repeated', 'repeti'),
    'guessed': ('guessed', 'adivinhei/supus'),
    'selected': ('selected', 'selecionei'),
    'clicked': ('clicked', 'cliquei'),
}

past_dict_keys = [word for word in past_dict]

past_dict_values = [word[1] for word in past_dict.values()]

past_dict_uniques = {
    'was': ('was', 'era/fui/estava'),
    'were': ('were', 'eram/estavam'),
    'had': ('had', 'tinha/tive'),
    'did': ('did', 'fiz')
}

# 'was', 'were', 'had', 'did',
past = [
    'said', 'went',
    'got', 'made', 'knew', 'thought', 'took', 'saw',
    'came', 'wanted', 'looked', 'used', 'found', 'gave', 'told',
    'worked', 'called', 'tried', 'asked', 'needed',
    'felt', 'became', 'left', 'put', 'meant', 'kept',
    'let', 'began', 'seemed', 'helped', 'talked', 'turned',
    'started', 'showed', 'heard', 'played', 'ran', 'moved', 'liked',
    'lived', 'believed', 'held', 'brought', 'happened', 'wrote',
    'provided', 'sat', 'stood', 'lost', 'paid', 'met',
    'included', 'continued', 'set', 'learned', 'changed', 'led',

    'understood', 'watched', 'followed',
    'stopped', 'created', 'spoke', 'read', 'allowed', 'added', 'spent',
    'grew', 'opened', 'walked', 'won', 'offered', 'remembered',
    'loved', 'considered', 'appeared', 'bought', 'waited', 'served', 'died', 'sent',
    'expected', 'built', 'stayed', 'fell', 'cut', 'reached', 'killed',
    'remained', 'suggested', 'rose', 'passed', 'sold', 'required',
    'reported', 'decided', 'pulled', 'broke', 'acquired', 'realized',
    'managed', 'developed', 'trusted', 'imagined', 'stepped', 'regreted', 'manipulated',
    'dreamed', 'discussed', 'drank', 'ate', 'skept', 'saw', 'repeated', 'knew',
    'guessed', 'selected', 'clicked',
]

# 'era/estava/fiquei', 'eram/estavam/ficaram', 'possui/tive', 'fiz',
past_pt_br = [
    'disse/falei', 'fui',
    'adquiri/consegui/obtive/peguei', 'criei/fiz', 'conheci/sabia', 'achei/pensei', 'levei/peguei/tomei', 'vi',
    'cheguei/vim', 'pretendia/queria', 'olhei/vi', 'usei', 'achei/encontrei', 'dei', 'contei/disse',
    'funcionei/trabalhei', 'chamei/telefonei', 'experimentei/tentei', 'pedi/perguntei', 'necessitei/precisei',
    'senti', 'me tornei', 'abandonei/deixei/sai', 'coloquei/pus', 'signifiquei', 'continuei/guardei/mantive',
    'deixei/permiti', 'começei/iniciei', 'pareci', 'ajudei/auxiliei', 'conversei/falei', 'transformei/virei',
    'começei/iniciei', 'apresentei/mostrei', 'escutei/ouvi', 'joguei/toquei', 'corri', 'movi/mexi', 'gostei',
    'morei/vivi', 'acreditei/cri', 'mantive/segurei', 'trouxe', 'aconteci/ocorri', 'escrevi',
    'forneci/proporcionei', 'sentei', 'levantei/permaneci', 'perdi', 'paguei', 'conheci/encontrei/reuni',
    'inclui', 'continuei', 'configurei/defini/estabeleci/pus', 'aprendi', 'alterei/mudei', 'conduzi/liderei',

    'compreender/entender', 'olhar/observar/ver', 'acompanhar/seguir',
    'impedir/parar', 'criar', 'conversar/falar', 'ler', 'autorizar/permitir', 'acrescentar/adicionar', 'gastar/passar',
    'aumentar/crescer', 'abrir', 'andar/caminhar', 'ganhar/vencer', 'oferecer/propor', 'lembrar/recordar',
    'adorar/amar', 'considerar', 'aparecer', 'comprar', 'esperar', 'servir', 'falecer/morrer', 'enviar/mandar',
    'esperar', 'construir', 'ficar/permanecer', 'cair', 'cortar', 'alcançar/atingir/chegar a', 'matar',
    'ficar/permanecer', 'sugerir', 'aumentar/criar alguém,algo/levantar', 'passar', 'vender', 'exigir/necessitar',
    'relatar/reportar', 'decidir', 'puxar', 'romper/quebrar', 'adquirir/comprar/obter', 'perceber/realizar',
    'administrar/gerir', 'crescer/desenvolver', 'confiar', 'imaginar', 'pisar', 'arrepender/lamentar', 'manipular',
    'sonhar', 'debater/discutir', 'beber', 'comer', 'pular/saltar', 'ver', 'repetir', 'conhecer/saber',
    'adivinhar/supor', 'selecionar', 'clicar',
]

if __name__ == '__main__':
    # print(verify('placed', 'managed', database=past))

    # bricks = '=' * 100
    #
    # print('\n')
    #
    # print(bricks)
    # print(f'{len(past) = }')
    # print(f'{len(past_pt_br) = }')
    #
    # print('\n')
    # for word in zip(past, past_pt_br):
    #     print(word)

    counter = 0
    while counter < len(past):
        # print(f"{verbs_inf[counter]}_ = ['{verbs_inf[counter]}', '{verbs_inf_pt_br[counter]}']")
        print(f"'{past[counter]}': ('{past[counter]}', '{past_pt_br[counter]}'),")
        counter += 1
    print(len(past_dict))