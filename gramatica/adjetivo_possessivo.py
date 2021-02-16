

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
adj_pos_u = ['My', 'Your', 'His', 'Her', 'Its', 'Our', 'Their']

adj_pos_l = ['my', 'your', 'his', 'her', 'its', 'our', 'their']

adj_pos_pt_br = [
    'meu(s)/minha(s)', 'seu(s)/sua(s)', 'dele(s)', 'dela(s)', 'dele(s)/dela(s)', 'nosso(s)/nossa(s)s', 'dele(s)/dela(s)'
]

my_ = ['my', 'meu(s)/minha(s)']
your_ = ['your', 'seu(s)/sua(s)']
his_ = ['his', 'dele(s)']
her_ = ['her', 'dela(s)']
its_ = ['its', 'dele(s)/dela(s)']
our_ = ['our', 'nosso(s)/nossa(s)s']
their_ = ['their', 'dele(s)/dela(s)']


if __name__ == '__main__':
    bricks = '=' * 100

    print('\n')
    print(bricks)
    print(f'{len(adj_pos_l) = }')
    print(f'{len(adj_pos_pt_br) = }')

    print('\n')
    for word in zip(adj_pos_l, adj_pos_pt_br):
        print(word)

    print('\n')
    counter = 0
    while counter < len(adj_pos_l):
        print(f"{adj_pos_l[counter]}_ = ['{adj_pos_l[counter]}', '{adj_pos_pt_br[counter]}']")
        counter += 1
