

from criar_frase import sentence_maker as _

from traduzir import do_translation as do

from banco_de_dados import *

colors: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
)

x = ' '
print('\n')
arrow = '-> '
paint = colors[4]
blue = colors[7]

"----------------------------------------------- FRASES COM 3 ELEMENTOS -----------------------------------------------"

"He loves cars"
this3_1 = _(pro_sgl_others_u, x, pst_sgl, x, nouns_pl)
print([3.1], f'{paint}{this3_1}{blue}')  # , arrow, do(this3_1, 'pt')

"They love cars"
this3_2 = _(pro_pl_others_u, x, pst_pl, x, nouns_pl)
print([3.2], f'{paint}{this3_2}{blue}')  # , arrow, do(this3_2, 'pt')

"Dogs love cars"
this3_3 = _(nouns_pl, x, pst_pl, x, nouns_pl)
print([3.3], f'{paint}{this3_3}{blue}')  # , arrow, do(this3_3, 'pt')

"She normally drinks"
this3_4 = _(pro_sgl_others_u, x, adv_frequency, x, pst_sgl)
print([3.4], f'{paint}{this3_4}{blue}')  # , arrow, do(this3_4, 'pt')

"They normally drink"
this3_5 = _(pro_pl_others_u, x, adv_frequency, x, pst_pl)
print([3.5], f'{paint}{this3_5}{blue}')  # , arrow, do(this3_5, 'pt')

"People normally drink"
this3_6 = _(nouns_pl, x, adv_frequency, x, pst_pl)
print([3.6], f'{paint}{this3_6}{blue}')  # , arrow, do(this3_6, 'pt')

"She loves them"
this3_7 = _(pro_sgl_others_u, x, pst_sgl, x, pro_obj)
print([3.7], f'{paint}{this3_7}{blue}')  # , arrow, do(this3_7, 'pt')

# "The dog barks"
# this3_4 = _(the_the_u, x, nouns_sgl, x, pst_sgl)
# print([3.4], f'{paint}{this3_4}{blue}')  # , arrow, do(this3_4, 'pt')
#
# "I love him"
# this3_5 = _(pro_sgl_others_u, x, pst_sgl, x, pro_obj)
# print([3.5], f'{paint}{this3_5}{blue}')  # , arrow, do(this3_5, 'pt')
#
# "I am funny"
# this3_6 = _(i_u, x, am_l, x, adj)
# print([3.6], f'{paint}{this3_6}{blue}')  # , arrow, do(this3_6, 'pt')
#
# "She is angry"
# this3_7 = _(pro_sgl_others_u, x, is_l, x, adj)
# print([3.7], f'{paint}{this3_7}{blue}')  # , arrow, do(this3_7, 'pt')
#
# "You are angry"
# this3_8 = _(pro_pl_u, x, are_l, x, adj)
# print([3.8], f'{paint}{this3_8}{blue}')  # , arrow, do(this3_8, 'pt')
#
# "The clean water"
# # this3_5 = _(the_the_u, x, adj, x, nouns)
# # print([3.5], f'{paint}{this3_5}{blue}')  # , arrow, do(this3_5, 'pt')

"----------------------------------------------- FRASES COM 4 ELEMENTOS -----------------------------------------------"
# #todo Frase com 4 elementos (singular)
# "He loves the cars"
# this4 = _(pro_sgl_others_u, x, pst_sgl, x, the_the_l, x, nouns_pl)
# print([4], f'{paint}{this4}{blue}')  # , arrow, do(this4, 'pt')
#
# #todo Frase com 4 elementos (plural)
# "They love the cars"
# this4_1 = _(pro_pl_others_u, x, pst_pl, x, the_the_l, x, nouns_pl)
# print([4.1], f'{paint}{this4_1}{blue}')  # , arrow, do(this4_1, 'pt')
#
# "She eventually drinks water"
# this4_2 = _(pro_sgl_others_u, x, adv_frequency, x, pst_sgl, x, nouns_sgl)
# print([4.2], f'{paint}{this4_2}{blue}')  # , arrow, do(this4_2, 'pt')
#
# "They eventually drink water"
# this4_3 = _(pro_pl_others_u, x, adv_frequency, x, pst_pl, x, nouns_pl)
# print([4.3], f'{paint}{this4_3}{blue}')  # , arrow, do(this4_3, 'pt')
















"                 the           dog           eats        the           rabbit"
# this_sentence = _(the_the_u, x, nouns_sgl, x, pst_sgl, x, the_the_l, x, nouns_sgl)
# print(f'{paint}{this_sentence}{blue}', arrow, do_translation(text=this_sentence, target_language='pt'))

"                  Those         dogs         eat        rabbits"
# this_sentence2 = _(demo_pl_u, x, nouns_pl, x, pst_pl, x, nouns_pl)
# print(f'{paint}{this_sentence2}{blue}', arrow, do_translation(text=this_sentence2, target_language='pt'))

"                  Her           ideas        are       stupid"
# this_sentence3 = _(adj_pos_u, x, nouns_pl, x, are_l, x, adj)
# print(f'{paint}{this_sentence3}{blue}', arrow, do_translation(text=this_sentence3, target_language='pt'))

"My car drives her"
# this_sentence4 = _(adj_pos_u, x, nouns_pl, x, pst_pl, x, pro_obj)
# print(f'{paint}{this_sentence4}{blue}', arrow, do_translation(text=this_sentence4, target_language='pt'))

""
# this_sentence5 = _(names, x, and_, x, names, x, pst_pl, x, adv_ly, x, the_the_l, x, nouns)
# print(f'{paint}{this_sentence5}{blue}', arrow, do_translation(text=this_sentence5, target_language='pt'))
