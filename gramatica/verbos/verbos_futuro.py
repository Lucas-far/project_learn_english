

from gramatica.verbos.verbos_presente_pl import pst_pl_dict_keys
from gramatica.verbos.verbos_infinitivo import verbs_inf_dict_values

fut_dict = {
    'will say': ('will say', 'direi/falarei'),
    'will go': ('will go', 'irei'),
    'will get': ('will get', 'adquirirei/conseguirei/obterei/pegarei'),
    'will make': ('will make', 'criarei/farei'),
    'will know': ('will know', 'conhecerei/saberei'),
    'will think': ('will think', 'acharei/pensarei'),
    'will take': ('will take', 'levarei/pegarei/tomarei'),
    'will see': ('will see', 'verei'),
    'will come': ('will come', 'chegarei/virei'),
    'will want': ('will want', 'pretenderei/quererei'),
    'will look': ('will look', 'olharei/verei'),
    'will use': ('will use', 'usarei'),
    'will find': ('will find', 'acharei/encontrarei'),
    'will give': ('will give', 'darei'),
    'will tell': ('will tell', 'contarei/direi'),
    'will work': ('will work', 'funcionarei/trabalharei'),
    'will call': ('will call', 'chamarei/telefonarei'),
    'will try': ('will try', 'experimentarei/tentarei'),
    'will ask': ('will ask', 'pedirei/perguntarei'),
    'will need': ('will need', 'necessitarei/precisarei'),
    'will feel': ('will feel', 'sentirei'),
    'will become': ('will become', 'tornarei'),
    'will leave': ('will leave', 'abandonarei/deixarei/sairei'),
    'will put': ('will put', 'colocarei/porei'),
    'will mean': ('will mean', 'significarei'),
    'will keep': ('will keep', 'continuarei/guardarei/manterei'),
    'will let': ('will let', 'deixarei/permitirei'),
    'will begin': ('will begin', 'começarei/iniciarei'),
    'will seem': ('will seem', 'parecerei'),
    'will help': ('will help', 'ajudarei/auxiliarei'),
    'will talk': ('will talk', 'conversarei/falarei'),
    'will turn': ('will turn', 'transformarei/virarei'),
    'will start': ('will start', 'começarei/iniciarei'),
    'will show': ('will show', 'apresentarei/mostrarei'),
    'will hear': ('will hear', 'escutarei/ouvirei'),
    'will play': ('will play', 'jogarei/tocarei'),
    'will run': ('will run', 'correrei'),
    'will move': ('will move', 'moverei/mexerei'),
    'will like': ('will like', 'gostarei'),
    'will live': ('will live', 'morarei/viverei'),
    'will believe': ('will believe', 'acreditarei/crerei'),
    'will hold': ('will hold', 'manterei/segurarei'),
    'will bring': ('will bring', 'trarei'),
    'will happen': ('will happen', 'acontecerei/ocorrerei'),
    'will write': ('will write', 'escreverei'),
    'will provide': ('will provide', 'fornecerei/proporcionarei'),
    'will sit': ('will sit', 'sentarei'),
    'will stand': ('will stand', 'levantarei/permanecerei'),
    'will lose': ('will lose', 'perderei'),
    'will pay': ('will pay', 'pagarei'),
    'will meet': ('will meet', 'conhecerei/encontrarei'),
    'will include': ('will include', 'incluirei'),
    'will continue': ('will continue', 'continuarei'),
    'will set': ('will set', 'configurarei/definirei/estabelecerei/porei'),
    'will learn': ('will learn', 'aprenderei'),
    'will change': ('will change', 'alterarei/mudarei'),
    'will lead': ('will lead', 'conduzirei/liderarei'),
    'will understand': ('will understand', 'compreenderei/entenderei'),
    'will watch': ('will watch', 'olharei/observarei/verei'),
    'will follow': ('will follow', 'acompanharei/seguirei'),
    'will stop': ('will stop', 'impedirei/pararei'),
    'will create': ('will create', 'criarei'),
    'will speak': ('will speak', 'conversarei/falarei'),
    'will read': ('will read', 'lerei'),
    'will allow': ('will allow', 'autorizarei/permitirei'),
    'will add': ('will add', 'acrescentarei/adicionarei'),
    'will spend': ('will spend', 'gastarei/passarei'),
    'will grow': ('will grow', 'aumentarei/crescerei'),
    'will open': ('will open', 'abrirei'),
    'will walk': ('will walk', 'andarei/caminharei'),
    'will win': ('will win', 'ganharei/vencerei'),
    'will offer': ('will offer', 'oferecerei/proporei'),
    'will remember': ('will remember', 'lembrarei/recordarei'),
    'will love': ('will love', 'adorarei/amarei'),
    'will consider': ('will consider', 'considerarei'),
    'will appear': ('will appear', 'aparecerei'),
    'will buy': ('will buy', 'comprarei'),
    'will wait': ('will wait', 'esperarei'),
    'will serve': ('will serve', 'servirei'),
    'will die': ('will die', 'falecerei/morrerei'),
    'will send': ('will send', 'enviarei/mandarei'),
    'will expect': ('will expect', 'esperarei'),
    'will build': ('will build', 'construirei'),
    'will stay': ('will stay', 'ficarei/permanecerei'),
    'will fall': ('will fall', 'cairei'),
    'will cut': ('will cut', 'cortarei'),
    'will reache': ('will reache', 'alcançarei/atingirei/chegarei a'),
    'will kill': ('will kill', 'matarei'),
    'will remain': ('will remain', 'ficarei/permanecerei'),
    'will suggest': ('will suggest', 'irei sugerir'),
    'will raise': ('will raise', 'aumentarei/criarei alguém,algo/levantarei'),
    'will pass': ('will pass', 'passarei'),
    'will sell': ('will sell', 'venderei'),
    'will require': ('will require', 'exigirei/necessitarei'),
    'will report': ('will report', 'relatarei/reportarei'),
    'will decide': ('will decide', 'decidirei'),
    'will pull': ('will pull', 'puxarei'),
    'will break': ('will break', 'romperei/quebrarei'),
    'will acquire': ('will acquire', 'adquirirei/comprarei/obterei'),
    'will realize': ('will realize', 'perceberei/realizarei'),
    'will manage': ('will manage', 'administrarei/irei gerir'),
    'will develop': ('will develop', 'crescerei/desenvolverei'),
    'will trust': ('will trust', 'confiarei'),
    'will imagine': ('will imagine', 'imaginarei'),
    'will step': ('will step', 'pisarei'),
    'will regret': ('will regret', 'arrependerei/lamentarei'),
    'will manipulate': ('will manipulate', 'manipularei'),
    'will dream': ('will dream', 'sonharei'),
    'will discuss': ('will discuss', 'debaterei/discutirei'),
    'will drink': ('will drink', 'beberei'),
    'will eat': ('will eat', 'comerei'),
    'will skip': ('will skip', 'pularei/saltarei'),
    'will repeat': ('will repeat', 'repetirei'),
    'will guess': ('will guess', 'adivinharei/irei supor'),
    'will select': ('will select', 'selecionarei'),
    'will click': ('will click', 'clicarei'),
}

fut_dict_keys = [word for word in fut_dict]

fut_dict_values = [word[1] for word in fut_dict.values()]

fut_dict_uniques = {}

if __name__ == '__main__':
    # counter = 0
    # while counter < len(pst_pl_dict_keys):
    #     # print(f"{verbs_inf[counter]}_ = ['{verbs_inf[counter]}', '{verbs_inf_pt_br[counter]}']")
    #     print(f"'will {pst_pl_dict_keys[counter]}': ('will {pst_pl_dict_keys[counter]}', '{verbs_inf_dict_values[counter]}'),")
    #     counter += 1
    print(fut_dict)
    print(len(fut_dict))
