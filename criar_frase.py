

from random import choice

def sentence_maker(*args):  # removed parameter: example
    """"""
    sentence = []

    for word in args:
        sentence.append(choice(word))
        # print(f'{colors[4]}{choice(word)}{colors[7]}', end='')
    return "".join(sentence)
    # print('\n')
    # print(example)

if __name__ == '__main__':
    pass
