

from criar_frase import sentence_maker as _
from banco_de_dados import *

c: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
)

x = ' '
arrow = '-> '
paint, blue = c[4], c[7]

##
syntax932 = f'\nPronome I + {c[3]}to be{c[7]} + advérbio + adjetivo'  # I am actually glad
var932 = _(i_u, x, am_l, x, adv_ly, x, adj)
print(f'{syntax932} -> {paint}{var932}{blue}')  # 932

##
syntax685 = f'Pronomes he/she/it + {c[3]}to be{c[7]} + advérbio + adjetivo'  # He is actually glad
var685 = _(pro_sgl_others_u, x, is_l, x, adv_ly, x, adj)
print(f'{syntax685} -> {paint}{var685}{blue}')  # 685

##
syntax958 = f'Pronomes we/you/they + {c[3]}to be{c[7]} + advérbio + adjetivo'  # We are actually glad
var958 = _(pro_pl_u, x, are_l, x, adv_ly, x, adj)
print(f'{syntax958} -> {paint}{var958}{blue}')  # 958

##
syntax178 = f'{c[3]}to be{c[7]} + pronome I + advérbio de frequência + adjetivo'  # Am I crazy?
var178 = _(am_u, x, i_u, x, adv_frequency, x, adj, '?')
print(f'{syntax178} -> {paint}{var178}{blue}')  # 178

##
syntax436 = f'{c[3]}to be{c[7]} + pronomes he/she/it + advérbio de frequência + adjetivo'  # Is she crazy?
var436 = _(is_u, x, pro_sgl_others_l, x, adv_frequency, x, adj, '?')
print(f'{syntax436} -> {paint}{var436}{blue}')  # 436

##
syntax552 = f'{c[3]}to be{c[7]} + pronomes we/you/they + advérbio de frequência + adjetivo'  # Are you crazy?
var552 = _(are_u, x, pro_pl_l, x, adv_frequency, x, adj, '?')
print(f'{syntax552} -> {paint}{var552}{blue}')  # 552

##
syntax381 = f'Substantivo plural + {c[3]}to be{c[7]} + advérbio + adjetivo'  # Dogs are clearly cute
var381 = _(nouns_pl, x, are_l, x, adv_gl, x, adj)
print(f'{syntax381} -> {paint}{var381}{blue}')  # 381

##
syntax582 = f'{c[3]}to be{c[7]} + substantivo plural + advérbio + adjetivo'  # Are dogs clearly cute?
var582 = _(are_l, x, nouns_pl, x, adv_gl, x, adj, '?')
print(f'{syntax582} -> {paint}{var582}{blue}')  # 582
