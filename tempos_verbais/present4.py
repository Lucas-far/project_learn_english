

from criar_frase import sentence_maker as _
from banco_de_dados import *

c: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
)

x = ' '
arrow = '-> '
paint, blue = c[4], c[7]

##
print(f'\nPronome + {c[3]}verbo to be no presente{c[7]} + advérbio + adjetivo')
"I am actually glad"
var932 = _(i_u, x, am_l, x, adv_ly, x, adj)
print(f'{paint}{var932}{blue}')  # 666

"He is actually glad"
var685 = _(pro_sgl_others_u, x, is_l, x, adv_ly, x, adj)
print(f'{paint}{var685}{blue}')  # 797

"We are actually glad"
var958 = _(pro_pl_u, x, are_l, x, adv_ly, x, adj)
print(f'{paint}{var958}{blue}')  # 898





##
print(f'\n{c[3]}verbo to be no presente{c[7]} + pronome + advérbio de frequência + adjetivo')
"Is she crazy?"
var436 = _(is_u, x, pro_sgl_others_l, x, adv_frequency, x, adj, '?')
print(f'{paint}{var436}{blue}')  # 436

"Are you crazy?"
var552 = _(are_u, x, pro_pl_l, x, adv_frequency, x, adj, '?')
print(f'{paint}{var552}{blue}')  # 552

"Am I crazy?"
var178 = _(am_u, x, i_u, x, adv_frequency, x, adj, '?')
print(f'{paint}{var178}{blue}')  # 178





##
"Dogs are clearly cute"
print(f'\nSubstantivo no plural + {c[3]}verbo to be no presente{c[7]} + advérbio + adjetivo')
var381 = _(nouns_pl, x, are_l, x, adv_gl, x, adj)
print(f'{paint}{var381}{blue}')  # 381
