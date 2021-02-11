

from criar_frase import sentence_maker as _

from traduzir import do_translation as do

from banco_de_dados import *

c: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
)

x = ' '
print('\n')
arrow = '-> '
paint = c[4]
blue = c[7]

"----------------------------------------------- FRASES COM 3 ELEMENTOS -----------------------------------------------"

##
print(f'\nPronome + {c[3]}verbo to be no presente{c[7]} + adjetivo')

"I am glad"
var932 = _(i_u, x, am_l, x, adj)
print(f'{paint}{var932}{blue}', arrow, do(var932, 'pt'))  # 932

"He is glad"
var685 = _(pro_sgl_others_u, x, is_l, x, adj)
print(f'{paint}{var685}{blue}', arrow, do(var685, 'pt'))  # 685

"We are glad"
var958 = _(pro_pl_u, x, are_l, x, adj)
print(f'{paint}{var958}{blue}', arrow, do(var958, 'pt'))  # 958





##
print(f'\n{c[3]}verbo to be no presente{c[7]} + pronome + adjetivo')
"Is she crazy?"
var436 = _(is_u, x, pro_sgl_others_l, x, adj, '?')
print(f'{paint}{var436}{blue}', arrow, do(var436, 'pt'))  # 436

"Are you crazy?"
var552 = _(are_u, x, pro_pl_l, x, adj, '?')
print(f'{paint}{var552}{blue}', arrow, do(var552, 'pt'))  # 552

"Am I crazy?"
var178 = _(am_u, x, i_u, x, adj, '?')
print(f'{paint}{var178}{blue}', arrow, do(var178, 'pt'))  # 178





##
"Dogs are cute"
print(f'\nSubstantivo no plural + {c[3]}verbo to be no presente{c[7]} + adjetivo')
var381 = _(nouns_pl, x, are_l, x, adj)
print(f'{paint}{var381}{blue}', arrow, do(var381, 'pt'))  # 381





##
print(f'\n{c[3]}verbo to be no presente{c[7]} + substantivo + adjetivo')
"Are dogs cute?"
var582 = _(are_l, x, nouns_pl, x, adj, '?')
print(f'{paint}{var582}{blue}', arrow, do(var582, 'pt'))  # 582




##
print(f'\nPronome demonstrativo + {c[3]}verbo to be no presente{c[7]} + adjetivo')
"This is ridiculous"
var99 = _(demo_sgl_u, x, is_l, x, adj)
print(f'{paint}{var99}{blue}', arrow, do(var99, 'pt'))  # 99

"Those are ridiculous"
var324 = _(demo_pl_u, x, are_l, x, adj)
print(f'{paint}{var324}{blue}', arrow, do(var324, 'pt'))  # 324




##
print(f'\n{c[3]}verbo to be no presente{c[7]} + pronome demonstrativo + adjetivo')
"Is this ridiculous?"
var359 = _(is_u, x, demo_sgl_l, x, adj, '?')
print(f'{paint}{var359}{blue}', arrow, do(var359, 'pt'))  # 359

"Are those ridiculous?"
var941 = _(are_u, x, demo_pl_l, x, adj, '?')
print(f'{paint}{var941}{blue}', arrow, do(var941, 'pt'))  # 941





##
print(f'\nPergunta + {c[3]}verbo to be no presente{c[7]} + pronome')
"Who am I?"
var859 = _(wh_specific_u, x, am_l, x, i_u, '?')
print(f'{paint}{var859}{blue}', arrow, do(var859, 'pt'))  # 859

"Who is it?"
var106 = _(wh_specific_u, x, is_l, x, pro_sgl_others_l, '?')
print(f'{paint}{var106}{blue}', arrow, do(var106, 'pt'))  # 106

"Who are you?"
var367 = _(wh_specific_u, x, are_l, x, pro_pl_l, '?')
print(f'{paint}{var367}{blue}', arrow, do(var367, 'pt'))  # 367





"------------------------------------------- FRASES COM VERBOS NO PRESENTE -------------------------------------------"
##
# print(f'\nArtigo + substantivo + {c[3]}verbo no presente{c[7]}')
# "The dog runs"
# var514 = _(the_the_u, x, nouns_sgl, x, pst_sgl)
# print(f'{paint}{var514}{blue}', arrow, do(var, 'pt)
#
# "The dogs run"
# var946 = _(the_the_u, x, nouns_pl, x, pst_pl)
# print(f'{paint}{var946}{blue}', arrow, do(var, 'pt)





##
# print(f'\nPronome + {c[3]}verbo no presente{c[7]} + substantivo')
# "He loves cars"
# var267 = _(pro_sgl_others_u, x, pst_sgl, x, nouns_sgl)
# print(f'{paint}{var267}{blue}', arrow, do(var, 'pt)
#
# "They love cars"
# var324 = _(pro_pl_u, x, pst_pl, x, nouns_pl)
# print(f'{paint}{var324}{blue}', arrow, do(var, 'pt)
#
# "Dogs love cars"
# var823 = _(nouns_pl, x, pst_pl, x, nouns_pl)
# print(f'{paint}{var823}{blue}', arrow, do(var, 'pt)





##
print(f'\nPronome/Substantivo + {c[3]}verbo no presente{c[7]} + pronome objeto')
"She loves them"
var429 = _(pro_sgl_others_u, x, pst_sgl, x, pro_obj)
print(f'{paint}{var429}{blue}', arrow, do(var429, 'pt'))  # 429

"We love them"
var711 = _(pro_pl_others_u, x, pst_pl, x, pro_obj)
print(f'{paint}{var711}{blue}', arrow, do(var711, 'pt'))  # 711

"People love them"
var786 = _(nouns_pl, x, pst_pl, x, pro_obj)
print(f'{paint}{var786}{blue}', arrow, do(var786, 'pt'))  # 786






##
print(f'\nPronome/Substantivo + {c[3]}verbo no presente{c[7]} + pronome demonstrativo')
"She loves that"
var825 = _(pro_sgl_others_u, x, pst_sgl, x, demo_all_l)
print(f'{paint}{var825}{blue}', arrow, do(var825, 'pt'))  # 825

"We love this"
var339 = _(pro_pl_others_u, x, pst_pl, x, demo_all_l)
print(f'{paint}{var339}{blue}', arrow, do(var339, 'pt'))  # 339

"People love these"
var792 = _(nouns_pl, x, pst_pl, x, demo_all_l)
print(f'{paint}{var792}{blue}', arrow, do(var792, 'pt'))  # 792





##
print(f'\nPronome/Substantivo + advérbio de frequência + {c[3]}verbo no presente{c[7]}')
"She normally drinks"
var878 = _(pro_sgl_others_u, x, adv_frequency, x, pst_sgl)
print(f'{paint}{var878}{blue}', arrow, do(var878, 'pt'))  # 878

"They normally drink"
var834 = _(pro_pl_others_u, x, adv_frequency, x, pst_pl)
print(f'{paint}{var834}{blue}', arrow, do(var834, 'pt'))  # 834

"People normally drink"
var167 = _(nouns_pl, x, adv_frequency, x, pst_pl)
print(f'{paint}{var167}{blue}', arrow, do(var167, 'pt'))  # 167





##
print(f'\nVerbo auxiliar presente + pronome + {c[3]}verbo no presente{c[7]}')
"Does it work?"
var441 = _(the_does_u, x, pro_sgl_others_l, x, pst_pl, '?')
print(f'{paint}{var441}{blue}', arrow, do(var441, 'pt'))  # 441

"Do we work?"
var716 = _(the_do_u, x, pro_pl_others_l, x, pst_pl, '?')
print(f'{paint}{var716}{blue}', arrow, do(var716, 'pt'))  # 716





##
print(f'\nPronome/Substantivo + {c[3]}verbo can{c[7]} + {c[3]}verbo no presente{c[7]}')
"I can talk"
var241 = _(pro_gl_u, x, can_l, x, pst_pl)
print(f'{paint}{var241}{blue}', arrow, do(var241, 'pt'))  # 241




##
print(f'\nPronome + {c[3]}verbo has/have{c[7]} + substantivo')
"She has dolls"
var94 = _(pro_sgl_others_u, x, the_has_l, x, nouns_pl)
print(f'{paint}{var94}{blue}', arrow, do(var94, 'pt'))  # 94

"You have dolls"
var187 = _(pro_pl_others_u, x, the_have_l, x, nouns_pl)
print(f'{paint}{var187}{blue}', arrow, do(var187, 'pt'))  # 187





##
print(f'\nAdjetivo possessivo + adjetivo + substantivo')
"Her main idea"
var650 = _(adj_pos_u, x, adj, x, nouns_sgl)
print(f'{paint}{var650}{blue}', arrow, do(var650, 'pt'))  # 650

"Her main ideas"
var607 = _(adj_pos_u, x, adj, x, nouns_pl)
print(f'{paint}{var607}{blue}', arrow, do(var607, 'pt'))  # 607





##
print(f'\nArtigo + adjetivo + substantivo')
"The crying boy"
var862 = _(the_the_u, x, adj, x, nouns_sgl)
print(f'{paint}{var862}{blue}', arrow, do(var862, 'pt'))  # 862

"The crying boys"
var936 = _(the_the_u, x, adj, x, nouns_pl)
print(f'{paint}{var936}{blue}', arrow, do(var936, 'pt'))  # 936
