

pst_sgl_dict = {
    'says': ('says', 'diz/fala'),
    'goes': ('goes', 'vem'),
    'gets': ('gets', 'adquire/consegue/obtem/pega'),
    'makes': ('makes', 'cria/faz'),
    'knows': ('knows', 'conhece/sabe'),
    'thinks': ('thinks', 'acha/pensa'),
    'takes': ('takes', 'leva/pega/toma'),
    'sees': ('sees', 'vê'),
    'comes': ('comes', 'chega/vêm'),
    'wants': ('wants', 'pretende/quer'),
    'looks': ('looks', 'olha/vê'),
    'uses': ('uses', 'usa'),
    'finds': ('finds', 'acha/encontra'),
    'gives': ('gives', 'dá'),
    'tells': ('tells', 'conta/diz'),
    'works': ('works', 'funciona/trabalha'),
    'calls': ('calls', 'chama/telefona'),
    'tries': ('tries', 'experimenta/tenta'),
    'asks': ('asks', 'pede/pergunta'),
    'needs': ('needs', 'necessita/precisa'),
    'feels': ('feels', 'sente'),
    'becomes': ('becomes', 'torna-se'),
    'leaves': ('leaves', 'abandona/deixa/sai'),
    'puts': ('puts', 'coloca/põe'),
    'means': ('means', 'significa'),
    'keeps': ('keeps', 'continua/guarda/mantêm'),
    'lets': ('lets', 'deixa/permite'),
    'begins': ('begins', 'começa/inicia'),
    'seems': ('seems', 'parece'),
    'helps': ('helps', 'ajuda/auxilia'),
    'talks': ('talks', 'conversa/fala'),
    'turns': ('turns', 'transforma/vira'),
    'starts': ('starts', 'começa/inicia'),
    'shows': ('shows', 'apresenta/mostra'),
    'hears': ('hears', 'escuta/ouvi'),
    'plays': ('plays', 'joga/toca'),
    'runs': ('runs', 'corre'),
    'moves': ('moves', 'move/mexe'),
    'likes': ('likes', 'gosta'),
    'lives': ('lives', 'mora/vive'),
    'believes': ('believes', 'acredita/crê'),
    'holds': ('holds', 'mantêm/segura'),
    'brings': ('brings', 'traz'),
    'happens': ('happens', 'acontece/ocorre'),
    'writes': ('writes', 'escreve'),
    'provides': ('provides', 'fornece/proporciona'),
    'sits': ('sits', 'senta'),
    'stands': ('stands', 'levanta/permanece'),
    'loses': ('loses', 'perde'),
    'pays': ('pays', 'paga'),
    'meets': ('meets', 'conhece/encontra'),
    'includes': ('includes', 'inclui'),
    'continues': ('continues', 'continua'),
    'sets': ('sets', 'configura/define/estabelece/põe'),
    'learns': ('learns', 'aprende'),
    'changes': ('changes', 'altera/muda'),
    'leads': ('leads', 'conduz/lidera'),
    'understands': ('understands', 'compreende/entende'),
    'watches': ('watches', 'olha/observa/vê'),
    'follows': ('follows', 'acompanha/segue'),
    'stops': ('stops', 'impede/para'),
    'creates': ('creates', 'cria'),
    'speaks': ('speaks', 'conversa/fala'),
    'reads': ('reads', 'lê'),
    'allows': ('allows', 'autoriza/permite'),
    'adds': ('adds', 'acrescenta/adiciona'),
    'spends': ('spends', 'gasta/passa'),
    'grows': ('grows', 'aumenta/cresce'),
    'opens': ('opens', 'abre'),
    'walks': ('walks', 'anda/caminha'),
    'wins': ('wins', 'ganha/vence'),
    'offers': ('offers', 'oferece/propõe'),
    'remembers': ('remembers', 'lembra/recorda'),
    'loves': ('loves', 'adora/ama'),
    'considers': ('considers', 'considera'),
    'appears': ('appears', 'aparece'),
    'buys': ('buys', 'compra'),
    'waits': ('waits', 'espera'),
    'serves': ('serves', 'serve'),
    'dies': ('dies', 'falece/morre'),
    'sends': ('sends', 'envia/manda'),
    'expects': ('expects', 'espera'),
    'builds': ('builds', 'constroi'),
    'stays': ('stays', 'fica/permanece'),
    'falls': ('falls', 'cai'),
    'cuts': ('cuts', 'corta'),
    'reaches': ('reaches', 'alcança/atinge/chega'),
    'kills': ('kills', 'mata'),
    'remains': ('remains', 'fica/permanece'),
    'suggests': ('suggests', 'sugeri'),
    'raises': ('raises', 'aumenta/cria alguém,algo/levanta'),
    'passes': ('passes', 'passa'),
    'sells': ('sells', 'vende'),
    'requires': ('requires', 'exige/necessita'),
    'reports': ('reports', 'relata/reporta'),
    'decides': ('decides', 'decide'),
    'pulls': ('pulls', 'puxa'),
    'breaks': ('breaks', 'rompe/quebra'),
    'acquires': ('acquires', 'adquire/compra/obtém'),
    'realizes': ('realizes', 'percebe/realiza'),
    'manages': ('manages', 'administra/gere'),
    'develops': ('develops', 'cresce/desenvolve'),
    'trusts': ('trusts', 'confia'),
    'imagines': ('imagines', 'imagina'),
    'steps': ('steps', 'pisa'),
    'regrets': ('regrets', 'arrepende/lamenta'),
    'manipulates': ('manipulates', 'manipula'),
    'dreams': ('dreams', 'sonha'),
    'discusses': ('discusses', 'debate/discute'),
    'drinks': ('drinks', 'bebe'),
    'eats': ('eats', 'come'),
    'skips': ('skips', 'pula/salta'),
    'repeats': ('repeats', 'repete'),
    'guesses': ('guesses', 'adivinha/supõe'),
    'selects': ('selects', 'seleciona'),
    'clicks': ('clicks', 'clica'),
}

pst_sgl_dict_keys = [key for key in pst_sgl_dict]

pst_sgl_dict_values = [word[1] for word in pst_sgl_dict.values()]

pst_sgl_dict_uniques = {
    'is': ('is', 'é'),
    'has': ('has', 'possui/tem'),
    'does': ('does', 'faz'),
}

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

pst_sgl_pt_br = ['']

if __name__ == '__main__':
    bricks = '=' * 100
    # print(len(pst_sgl))
    # print(len(pst_sgl_dict))
    # print(pst_sgl_dict_keys)
    # counter = 0
    # while counter < len(pst_sgl):
    #     # print(f"{verbs_inf[counter]}_ = ['{verbs_inf[counter]}', '{verbs_inf_pt_br[counter]}']")
    #     print(f"'{pst_sgl[counter]}': ('{pst_sgl[counter]}', '{var[counter]}'),")
    #     counter += 1
    print('\n')
    print(bricks)
    print(f'{len(pst_sgl_dict) = }')
    print(f'{len(pst_sgl_dict_keys) = }')
    print(bricks)
    print(pst_sgl_dict)
    print(pst_sgl_dict_keys)
    print(pst_sgl_dict_values)
    pass
