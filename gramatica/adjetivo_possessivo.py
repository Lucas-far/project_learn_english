

adj_pos_gl_pt_br = [
    'meu(s)/minha(s)', 'seu(s)/sua(s)', 'dele(s)', 'dela(s)', 'dele/dela', 'nosso(s)/nossa(s)', 'dele(s)/dela(s)'
]

adj_pos_lvl_easy = ['my', 'your', 'his', 'her', 'its', 'our', 'their']

adj_pos_lvl_average = [
    'My', 'Your', 'His', 'Her', 'Its', 'Our', 'Their',
    'my', 'your', 'his', 'her', 'its', 'our', 'their'
]

adj_pos_gl = [
    'My', 'Your', 'His', 'Her', 'Its', 'Our', 'Their',
    'my', 'your', 'his', 'her', 'its', 'our', 'their'
]

# adjectives_possessive_upper = [index.replace(index[0], index[0].upper()) for index in adjectives_possessive_lower]
adj_pos_gl_u = ['My', 'Your', 'His', 'Her', 'Its', 'Our', 'Their']
adj_pos_gl_l = ['my', 'your', 'his', 'her', 'its', 'our', 'their']

if __name__ == '__main__':
    bricks = '=' * 100
    block = f'\n{bricks}\n'

    print('\n')

    print(bricks)

    print(f'{len(adj_pos_gl_pt_br) = }')
    print(f'{len(adj_pos_gl_l) = }')

    print(block)
    for x in zip(adj_pos_gl_pt_br, adj_pos_gl_l):
        print(x)
