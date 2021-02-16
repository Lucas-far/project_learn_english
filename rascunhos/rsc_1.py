

prep_direction_place_l = [
    'above', 'across', 'among', 'at', 'behind', 'below',
    'between', 'by', 'down', 'from', 'in',
    'in front of', 'on', 'over', 'through', 'to', 'towards',
    'under', 'up'
]

prep_direction_place_pt_br = [
    'acima/sobre (sem contato)', 'através', 'dentre/entre', 'em (sem contato)', 'atrás/detrás', 'abaixo/sob',
    'entre/no meio de', 'junto a/perto de/por', 'abaixo', 'de/do/desde/a partir de', 'em (contato dentro)',
    'em frente a/na frente de', 'em (contato fora)', 'acima/sobre (contato)', 'através de', 'para', 'em direção a',
    'debaixo/embaixo/por baixo', 'acima/em cima/para cima'
]

print('\n')
print(f'{len(prep_direction_place_l) = }')
print(f'{len(prep_direction_place_pt_br) = }')
print('\n')
for word in zip(prep_direction_place_l, prep_direction_place_pt_br):
    print(word)
