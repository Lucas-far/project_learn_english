

prep_short = [
    'at', 'by', 'down', 'for', 'from',
    'in', 'into', 'like', 'of', 'on', 'out',
    'over', 'to', 'up', 'with'
]

prep_short_pt_br = [
    'em (sem contato)', 'junto a/perto de/por', 'abaixo', 'para/por/durante', 'de/do/desde/a partir de',
    'em (contato dentro)', 'em/dentro/para dentro', 'como', 'de', 'em (contato fora)', 'para fora/fora',
    'acima/sobre (contato)', 'para', 'acima/em cima/para cima', 'com'
]

print('\n')
print(f'{len(prep_short) = }')
print(f'{len(prep_short_pt_br) = }')
print('\n')
for word in zip(prep_short, prep_short_pt_br):
    print(word)
