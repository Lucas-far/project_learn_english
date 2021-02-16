

prep_others = [
    'against', 'through', 'across', 'during', 'towards', 'without', 'about', 'after', 'until',
    'before', 'as', 'around', 'among', 'since'
]

prep_others_pt_br = [
    'contra', 'através de', 'através', 'durante', 'em direção a', 'sem', 'sobre/acerca de', 'depois', 'até',
    'diante de/perante', 'como', 'ao redor/em volta/por aí', 'dentre/entre', 'a partir de/desde'
]

print('\n')
print(f'{len(prep_others) = }')
print(f'{len(prep_others_pt_br) = }')
print('\n')
for word in zip(prep_others, prep_others_pt_br):
    print(word)
