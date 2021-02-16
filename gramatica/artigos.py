

art_gl_pt_br = ['um/uma/uns/umas', 'um/uma/uns/umas', 'a/as/o/os']
art_gl = ['The', 'the', 'A', 'an', ]
art_gl_u = ['A', 'An', 'The']
art_gl_l = ['a', 'an', 'the']
art_undef_u = ['A', 'An']
art_undef_l = ['a', 'an']
art_the_u = ['The']
art_the_l = ['the']

if __name__ == '__main__':
    bricks = '=' * 100
    block = f'\n{bricks}\n'

    print('\n')

    print(bricks)

    print(f'{len(art_gl_l) = }')
    print(f'{len(art_gl_pt_br) = }')

    print(block)
    for x in zip(art_gl_l, art_gl_pt_br):
        print(x)
