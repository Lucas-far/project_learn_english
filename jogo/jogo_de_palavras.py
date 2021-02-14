

from banco_de_dados import *
from cores import colors as x
from random import choice, shuffle
from traduzir import do_translation as traduza

"---------------------------------- TUTORIAL CRIAR ARQUIVOS DE VOCABULÁRIO SEPARADOS ----------------------------------"
""  # Criar um novo arquivo Python na pasta [ jogo ]
""  # O nome dado ao arquivo será importante para o próximo passo
""  # Em [ with open ], mude o primeiro argumento para o nome do arquivo criado
""  # Se quiser apenas criar vocabulário, desative todos os dados dentro do [ with open ], exceto o primeiro
""  # Em texto livre, começe a digitar o vocabulário

# ---------------------------------------------------- SUBSTANTIVO -----------------------------------------------------
substantivo = choice(nouns)
# substantivo_def = traduza(substantivo, 'pt')
# substantivo_tupla = f'("{substantivo}", "{substantivo_def}"), '  # dado a ser escrito no arquivo
# print(f'Substantivo: {x[4]}{substantivo}{x[7]}')

# -------------------------------------------------------- CAN ---------------------------------------------------------
can = choice(can_gl_suitable)
# can_def = traduza(can, 'pt')
# can_tupla = f'("{can}", "{can_def}"), '  # dado a ser escrito no arquivo
# print(f'Verbo "can": {x[4]}{can}{x[7]}')

# -------------------------------------------------------- HAVE --------------------------------------------------------
have = choice(have_gl_suitable)
# have_def = traduza(have, 'pt')
# have_tupla = f'("{have}", "{have_def}"), '  # dado a ser escrito no arquivo
# print(f'Verbo "have": {x[4]}{have}{x[7]}')

# --------------------------------------------------------- DO ---------------------------------------------------------
do = choice(do_gl_suitable)
# do_def = traduza(do, 'pt')
# do_tupla = f'("{do}", "{do_def}"), '  # dado a ser escrito no arquivo
# print(f'Verbo "do": {x[4]}{do}{x[7]}')

# ------------------------------------------------------- ARTIGO -------------------------------------------------------
artigo = choice(art_all_l)
# artigo_def = traduza(artigo, 'pt')
# artigo_tupla = f'("{artigo}", "{artigo_def}"), '  # dado a ser escrito no arquivo
# print(f'Artigo: {x[4]}{artigo}{x[7]}')

# ------------------------------------------------------ PRONOME -------------------------------------------------------
pronome = choice(pro_gl_l)
# pronome_def = traduza(pronome, 'pt')
# pronome_tupla = f'("{pronome}", "{pronome_def}"), '  # dado a ser escrito no arquivo
# print(f'Pronome: {x[4]}{pronome}{x[7]}')

# ------------------------------------------------------- TO BE --------------------------------------------------------
to_be = choice(to_be_pst_gl_suitable)
# to_be_def = traduza(to_be, 'pt')
# to_be_tupla = f'("{to_be}", "{to_be_def}"), '  # dado a ser escrito no arquivo
# print(f'Verbo "to be": {x[4]}{to_be}{x[7]}')

# ----------------------------------------------- PRONOME DEMONSTRATIVO ------------------------------------------------
pro_demonstrativo = choice(demo_gl_l)
# pro_demonstrativo_def = traduza(pro_demonstrativo, 'pt')
# pro_demonstrativo_tupla = f'("{pro_demonstrativo}", "{pro_demonstrativo_def}"), '  # dado a ser escrito no arquivo
# print(f'Pronome demonstrativo: {x[4]}{pro_demonstrativo}{x[7]}')

# ------------------------------------------------ ADJETIVO POSSESSIVO -------------------------------------------------
adj_possessivo = choice(adj_pos_gl_l)
# adj_possessivo_def = traduza(adj_possessivo, 'pt')
# adj_possessivo_tupla = f'("{adj_possessivo}", "{adj_possessivo_def}"), '  # dado a ser escrito no arquivo
# print(f'Pronome demonstrativo: {x[4]}{pro_demonstrativo}{x[7]}')


# ------------------------------------------------------- PT-EN --------------------------------------------------------
# pt_en = "farol"
# pt_en_def = traduza(pt_en, 'en')
# pt_en_tupla = f'("{pt_en}", "{pt_en_def}"), '  # dado a ser escrito no arquivo
# print(f'Palavra: {x[4]}{pt_en}{x[7]} -> Tradução: {x[3]}{pt_en_def}{x[7]}')

"----------------------------------------------------- ALGORITMO ------------------------------------------------------"

bricks = '=' * 20
break_row = '\n'
indent = '    '
difficulties = (
    f'{indent}1 - Fácil      (2 elementos)',
    f'{indent}2 - Simples    (3 elementos)',
    f'{indent}3 - Bom        (4 elementos)',
    f'{indent}4 - Legal      (5 elementos)',
    f'{indent}5 - Desafiador (6 elementos)',
    f'{indent}6 - Difícil    (7 elementos)',
    f'{indent}7 - Fluente    (8 elementos)'
)

report = """
    {} ELEMENTOS ESCOLHIDOS {}
    Escolhidos: {}{}{}
    Significados: {}{}{}
    """

for each_index in difficulties:
    print(each_index)

the_input = int(input('Escolha uma dificuldade\n-> '))

# ------------------------------------------------------- EN-PT --------------------------------------------------------
# en_pt = "english"
# en_pt_def = traduza(en_pt, 'pt')
# en_pt_tupla = f'("{en_pt}", "{en_pt_def}"), '  # dado a ser escrito no arquivo
# print(f'Palavra: {x[4]}{en_pt}{x[7]} -> Tradução: {x[3]}{en_pt_def}{x[7]}')

syntax = [
    substantivo, can, have, do, artigo, pronome, to_be, pro_demonstrativo, adj_possessivo
]

syntax_translated = [*syntax]

easy, simple, good, cool, challenging, hard, fluent = [], [], [], [], [], [], []

if the_input == 1 or the_input == 2 or the_input == 3 or the_input == 4 or the_input == 5 or the_input == 6 \
 or the_input == 7:
    shuffle(syntax)
    easy = [syntax[0], syntax[1]]
    simple = [*easy, syntax[2]]
    good = [*simple, syntax[3]]
    cool = [*good, syntax[4]]
    challenging = [*cool, syntax[5]]
    hard = [*challenging, syntax[6]]
    fluent = [*hard, syntax[7]]

if the_input == 1:
    translation = [str(traduza(each_index, 'pt')) for each_index in easy]
    print(report.format(bricks, bricks, x[4], easy, x[7], x[3], translation, x[7]))

elif the_input == 2:
    translation = [str(traduza(each_index, 'pt')) for each_index in simple]
    print(report.format(bricks, bricks, x[4], simple, x[7], x[3], translation, x[7]))

elif the_input == 3:
    translation = [str(traduza(each_index, 'pt')) for each_index in good]
    print(report.format(bricks, bricks, x[4], good, x[7], x[3], translation, x[7]))

elif the_input == 4:
    translation = [str(traduza(each_index, 'pt')) for each_index in cool]
    print(report.format(bricks, bricks, x[4], cool, x[7], x[3], translation, x[7]))

elif the_input == 5:
    translation = [str(traduza(each_index, 'pt')) for each_index in challenging]
    print(report.format(bricks, bricks, x[4], challenging, x[7], x[3], translation, x[7]))

elif the_input == 6:
    translation = [str(traduza(each_index, 'pt')) for each_index in hard]
    print(report.format(bricks, bricks, x[4], hard, x[7], x[3], translation, x[7]))

else:
    translation = [str(traduza(each_index, 'pt')) for each_index in fluent]
    print(report.format(bricks, bricks, x[4], fluent, x[7], x[3], translation, x[7]))


the_sentence = input(f'{break_row}Baseado no dado acima, escreva sua frase{break_row}-> ')
sentence_translated = traduza(the_sentence, 'pt')
sentence_report = f'("{the_sentence}", "{sentence_translated}"), \n'


with open('frases_salvas.txt', 'a') as py:
    py.write(sentence_report)
    # py.write(pt_en_tupla)              # adicionar uma tradução (pt para en)
    # py.write(en_pt_tupla)                # adicionar texto livre
    # py.write(substantivo_tupla)        # adicionar substantivo
    # py.write(can_tupla)                # adicionar uma forma do verbo can
    # py.write(have_tupla)               # adicionar uma forma do verbo have
    # py.write(artigo_tupla)             # adicionar um artigo
    # py.write(pronome_tupla)            # adicionar um pronome
    # py.write(to_be_tupla)              # adicionar uma forma do verbo to be
    # py.write(pro_demonstrativo_tupla)  # adicionar um pronome demonstrativo
