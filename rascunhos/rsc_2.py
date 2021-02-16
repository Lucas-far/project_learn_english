

# preposititons_phrasal_upper = [index.replace(index, index[0].upper() + index[1:]) for index in preposititons_phrasal_lower]
prep_phrasal_u = [
    'According to', 'Along with', 'Apart from', 'Because of', 'By means of', 'Contrary to', 'In addition to',
    'In front of', 'In reference to', 'In regard to', 'In spite of', 'Instead of', 'On account of', 'On top of',
    'Out of', 'With regard to'
]

prep_phrasal_l = [
    'according to', 'along with', 'apart from', 'because of', 'by means of', 'contrary to', 'in addition to',
    'in front of', 'in reference to', 'in regard to', 'in spite of', 'instead of', 'on account of', 'on top of',
    'out of', 'with regard to'
]

prep_phrasal_pt_br = [
    'de acordo com', 'junto com', 'além de', 'por causa de', 'por meio de', 'contrário a', 'além de',
    'na frente de', 'em referência a', 'em relação a', 'apesar de', 'em vez de', 'devido a', 'em cima de',
    'fora de', 'no que diz respeito ao(s)'
]

print('\n')
print(f'{len(prep_phrasal_u) = }')
print(f'{len(prep_phrasal_l) = }')
print(f'{len(prep_phrasal_pt_br) = }')
print('\n')
for word in zip(prep_phrasal_l, prep_phrasal_pt_br):
    print(word)
