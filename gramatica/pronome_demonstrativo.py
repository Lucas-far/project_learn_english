

pro_demo = [
    'this', 'these', 'that', 'those',
    'This', 'These', 'That', 'Those'
]

pro_demo_u = ['This', 'These', 'That', 'Those']
pro_demo_l = ['this', 'these', 'that', 'those']
pro_demo_pt_br = ['esse(a)', 'esses(as)', 'aquele(a)', 'aqueles(as)']

pro_demo_sgl_u = ['This', 'That']
pro_demo_sgl_l = ['this', 'that']

pro_demo_pl_u = ['These', 'Those']
pro_demo_pl_l = ['these', 'those']

this_u = ['This']
this_l = ['this']

these_u = ['These']
these_l = ['these']

that_u = ['That']
that_l = ['that']

those_u = ['Those']
those_l = ['those']

this_ = ['this', 'esse(a)']
these_ = ['these', 'esses(as)']
that_ = ['that', 'aquele(a)']
those_ = ['those', 'aqueles(as)']


if __name__ == '__main__':
    bricks = '=' * 100

    print('\n')
    print(bricks)
    print(f'{len(pro_demo_l) = }')
    print(f'{len(pro_demo_pt_br) = }')

    print('\n')
    for word in zip(pro_demo_l, pro_demo_pt_br):
        print(word)

    counter = 0
    while counter < len(pro_demo_l):
        print(f"{pro_demo_l[counter]}_ = ['{pro_demo_l[counter]}', '{pro_demo_pt_br[counter]}']")
        counter += 1
