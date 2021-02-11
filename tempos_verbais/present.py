

from criar_frase import sentence_maker as _

from traduzir import do_translation as do

from banco_de_dados import *

c: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
)

x = ' '
arrow = '-> '
paint, blue = c[4], c[7]

"4 elementos"
# Who are those people?
# The dog has paws
# I have to play

"5 elementos"
# The dog has to bark
"----------------------------------------------- FRASES COM 3 ELEMENTOS -----------------------------------------------"

##
print(f'\nPronome + {c[3]}verbo to be no presente{c[7]} + adjetivo')

"I am glad"
var932 = _(i_u, x, am_l, x, adj)
print(f'{paint}{var932}{blue}')  # 932

"He is glad"
var685 = _(pro_sgl_others_u, x, is_l, x, adj)
print(f'{paint}{var685}{blue}')  # 685

"We are glad"
var958 = _(pro_pl_u, x, are_l, x, adj)
print(f'{paint}{var958}{blue}')  # 958





##
print(f'\n{c[3]}verbo to be no presente{c[7]} + pronome + adjetivo')
"Is she crazy?"
var436 = _(is_u, x, pro_sgl_others_l, x, adj, '?')
print(f'{paint}{var436}{blue}')  # 436

"Are you crazy?"
var552 = _(are_u, x, pro_pl_l, x, adj, '?')
print(f'{paint}{var552}{blue}')  # 552

"Am I crazy?"
var178 = _(am_u, x, i_u, x, adj, '?')
print(f'{paint}{var178}{blue}')  # 178





##
"Dogs are cute"
print(f'\nSubstantivo no plural + {c[3]}verbo to be no presente{c[7]} + adjetivo')
var381 = _(nouns_pl, x, are_l, x, adj)
print(f'{paint}{var381}{blue}')  # 381





##
print(f'\n{c[3]}verbo to be no presente{c[7]} + substantivo + adjetivo')
"Are dogs cute?"
var582 = _(are_l, x, nouns_pl, x, adj, '?')
print(f'{paint}{var582}{blue}')  # 582




##
print(f'\nPronome demonstrativo + {c[3]}verbo to be no presente{c[7]} + adjetivo')
"This is ridiculous"
var99 = _(demo_sgl_u, x, is_l, x, adj)
print(f'{paint}{var99}{blue}')  # 99

"Those are ridiculous"
var324 = _(demo_pl_u, x, are_l, x, adj)
print(f'{paint}{var324}{blue}')  # 324




##
print(f'\n{c[3]}verbo to be no presente{c[7]} + pronome demonstrativo + adjetivo')
"Is this ridiculous?"
var359 = _(is_u, x, demo_sgl_l, x, adj, '?')
print(f'{paint}{var359}{blue}')  # 359

"Are those ridiculous?"
var941 = _(are_u, x, demo_pl_l, x, adj, '?')
print(f'{paint}{var941}{blue}')  # 941





##
print(f'\nPergunta + {c[3]}verbo to be no presente{c[7]} + pronome')
"Who am I?"
var859 = _(wh_specific_u, x, am_l, x, i_u, '?')
print(f'{paint}{var859}{blue}')  # 859

"Who is it?"
var106 = _(wh_specific_u, x, is_l, x, pro_sgl_others_l, '?')
print(f'{paint}{var106}{blue}')  # 106

"Who are you?"
var367 = _(wh_specific_u, x, are_l, x, pro_pl_l, '?')
print(f'{paint}{var367}{blue}')  # 367





"------------------------------------------- FRASES COM VERBOS NO PRESENTE -------------------------------------------"
##
# print(f'\nArtigo + substantivo + {c[3]}verbo no presente{c[7]}')
# "The dog runs"
# var514 = _(the_the_u, x, nouns_sgl, x, pst_sgl)
# print(f'{paint}{var514}{blue}')
#
# "The dogs run"
# var946 = _(the_the_u, x, nouns_pl, x, pst_pl)
# print(f'{paint}{var946}{blue}')





##
# print(f'\nPronome + {c[3]}verbo no presente{c[7]} + substantivo')
# "He loves cars"
# var267 = _(pro_sgl_others_u, x, pst_sgl, x, nouns_sgl)
# print(f'{paint}{var267}{blue}')
#
# "They love cars"
# var324 = _(pro_pl_u, x, pst_pl, x, nouns_pl)
# print(f'{paint}{var324}{blue}')
#
# "Dogs love cars"
# var823 = _(nouns_pl, x, pst_pl, x, nouns_pl)
# print(f'{paint}{var823}{blue}')





##
print(f'\nPronome/Substantivo + {c[3]}verbo no presente{c[7]} + pronome objeto')
"She loves them"
var429 = _(pro_sgl_others_u, x, pst_sgl, x, pro_obj)
print(f'{paint}{var429}{blue}')  # 429

"We love them"
var711 = _(pro_pl_others_u, x, pst_pl, x, pro_obj)
print(f'{paint}{var711}{blue}')  # 711

"People love them"
var786 = _(nouns_pl, x, pst_pl, x, pro_obj)
print(f'{paint}{var786}{blue}')  # 786






##
print(f'\nPronome/Substantivo + {c[3]}verbo no presente{c[7]} + pronome demonstrativo')
"She loves that"
var825 = _(pro_sgl_others_u, x, pst_sgl, x, demo_all_l)
print(f'{paint}{var825}{blue}')  # 825

"We love this"
var339 = _(pro_pl_others_u, x, pst_pl, x, demo_all_l)
print(f'{paint}{var339}{blue}')  # 339

"People love these"
var792 = _(nouns_pl, x, pst_pl, x, demo_all_l)
print(f'{paint}{var792}{blue}')  # 792





##
print(f'\nPronome/Substantivo + advérbio de frequência + {c[3]}verbo no presente{c[7]}')
"She normally drinks"
var878 = _(pro_sgl_others_u, x, adv_frequency, x, pst_sgl)
print(f'{paint}{var878}{blue}')  # 878

"They normally drink"
var834 = _(pro_pl_others_u, x, adv_frequency, x, pst_pl)
print(f'{paint}{var834}{blue}')  # 834

"People normally drink"
var167 = _(nouns_pl, x, adv_frequency, x, pst_pl)
print(f'{paint}{var167}{blue}')  # 167





##
print(f'\nVerbo auxiliar presente + pronome + {c[3]}verbo no presente{c[7]}')
"Does it work?"
var441 = _(the_does_u, x, pro_sgl_others_l, x, pst_pl, '?')
print(f'{paint}{var441}{blue}')  # 441

"Do we work?"
var716 = _(the_do_u, x, pro_pl_others_l, x, pst_pl, '?')
print(f'{paint}{var716}{blue}')  # 716





##
print(f'\nPronome/Substantivo + {c[3]}verbo can{c[7]} + {c[3]}verbo no presente{c[7]}')
"I can talk"
var241 = _(pro_gl_u, x, can_l, x, pst_pl)
print(f'{paint}{var241}{blue}')  # 241





##
print(f'\nPronome + {c[3]}verbo has/have{c[7]} + substantivo', '94 ' * 7)
"She has dolls"
var94 = _(pro_sgl_others_u, x, the_has_l, x, nouns_pl)
print(f'{paint}{var94}{blue}')  # 94

"You have dolls"
var187 = _(pro_pl_others_u, x, the_have_l, x, nouns_pl)
print(f'{paint}{var187}{blue}')  # 187




##
print(f'\nAdjetivo possessivo + adjetivo + substantivo')
"Her main idea"
var650 = _(adj_pos_u, x, adj, x, nouns_sgl)
print(f'{paint}{var650}{blue}')  # 650

"Her main ideas"
var607 = _(adj_pos_u, x, adj, x, nouns_pl)
print(f'{paint}{var607}{blue}')  # 607





##
print(f'\nArtigo + adjetivo + substantivo')
"The crying boy"
var862 = _(the_the_u, x, adj, x, nouns_sgl)
print(f'{paint}{var862}{blue}')  # 862

"The crying boys"
var936 = _(the_the_u, x, adj, x, nouns_pl)
print(f'{paint}{var936}{blue}')  # 936
