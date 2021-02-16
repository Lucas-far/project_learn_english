

pro_obj = ['me', 'you', 'him', 'her', 'it', 'us', 'them']

pro_obj_pt_br = ['me/ a mim', 'a você', 'a ele/lhe', 'a ela', 'a isso', 'a nós/nos', 'a eles/eles']

me_ = ['me', 'me/ a mim']
you_ = ['you', 'a você']
him_ = ['him', 'a ele/lhe']
her_ = ['her', 'a ela']
it_ = ['it', 'a isso']
us_ = ['us', 'a nós/nos']
them_ = ['them', 'a eles/eles']


if __name__ == '__main__':
    bricks = '=' * 100

    print('\n')
    print(bricks)
    print(f'{len(pro_obj) = }')
    print(f'{len(pro_obj_pt_br) = }')

    print('\n')
    for word in zip(pro_obj, pro_obj_pt_br):
        print(word)

    counter = 0
    while counter < len(pro_obj):
        print(f"{pro_obj[counter]}_ = ['{pro_obj[counter]}', '{pro_obj_pt_br[counter]}']")
        counter += 1
