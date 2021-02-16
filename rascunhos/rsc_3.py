

prep_time_l = [
    'on', 'ago', 'at', 'before', 'by', 'for',
    'from', 'in', 'since', 'to', 'until'
]

prep_time_pt_br = [
    'em (contato fora)', 'atrás', 'em (sem contato)', 'diante de/perante', 'junto a/perto de/por', 'para/por/durante',
    'de/do/desde/a partir de', 'em (contato dentro)', 'a partir de/desde', 'para', 'até'
]

print('\n')
print(f'{len(prep_time_l) = }')
print(f'{len(prep_time_pt_br) = }')
print('\n')
for word in zip(prep_time_l, prep_time_pt_br):
    print(word)
