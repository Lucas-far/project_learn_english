

prep_main = [
    'below', 'under', 'above', 'over',
    'behind', 'in front of', 'next to', 'between',
    'in', 'on', 'at'
]

prep_main_pt_br = [
    'abaixo/sob', 'debaixo/embaixo/por baixo', 'acima/sobre (sem contato)', 'acima/sobre (contato)',
    'atrás/detrás', 'em frente a/na frente de', 'ao lado de/próximo de', 'entre/no meio de',
    'em (contato dentro)', 'em (contato fora)', 'em (sem contato)'
]

print('\n')
print(f'{len(prep_main) = }')
print(f'{len(prep_main_pt_br) = }')
print('\n')
for word in zip(prep_main, prep_main_pt_br):
    print(word)