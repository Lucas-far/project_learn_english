from random import choice

from gramatica.substantivos.substantivo import nouns
from gramatica.adjetivo import adjectives

from gramatica.verbos.verbo import verbs_inf
from gramatica.verbos.verbo_presente_sgl import pst_sgl
from gramatica.verbos.verbo_presente_pl import pst_pl
from gramatica.verbos.verbo_passado import past
from gramatica.verbos.verbo_be import to_be_pst_gl_l

from gramatica.verbos.verbo_can import (can_pst_lvl_easy, can_pst_lvl_average, can_pst_lvl_fluent)

substantivo = choice(nouns)
adjetivo = choice(adjectives)

verbo_inf = choice(verbs_inf)
verbo_presente_para_singular = choice(pst_sgl)
verbo_presente_para_plural = choice(pst_pl)
verbo_passado = choice(past)
verbo_to_be_presente = choice(to_be_pst_gl_l)

verbo_can_presente = choice(can_pst_lvl_easy)
verbo_can_could_average = choice(can_pst_lvl_average)
verbo_can_could_fluent = choice(can_pst_lvl_fluent)

lista = [
    substantivo, adjetivo, verbo_inf, verbo_presente_para_singular, verbo_presente_para_plural, verbo_passado,
    verbo_to_be_presente,
]
print(lista)
print('\n' * 3)
input('ENTER')
# substantivo = choice(nouns)
# can = choice(can_gl_suitable)
# have = choice(have_gl_suitable)
# do = choice(do_gl_suitable)
# artigo = choice(art_all_l)
# pronome = choice(pro_gl_l)
# to_be = choice(to_be_pst_gl_suitable)
# pro_demonstrativo = choice(demo_gl_l)
# adj_possessivo = choice(adj_pos_gl_l)

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
syntax = [
    substantivo, can, have, do, artigo, pronome, to_be, pro_demonstrativo, adj_possessivo
]


easy, simple, good, cool, challenging, hard, fluent = [], [], [], [], [], [], []
