

from gramatica.substantivo import nouns, substantivos
from metodos.metodos import *
from random import choice, shuffle
from cores import colors as x

break_row = '\n'
ident = '    '
bricks = '=' * 20
success = f'{break_row}{x[3]}Respota correta{x[7]}{break_row}'
failure = f'{break_row}{x[1]}Respota incorreta{x[7]}{break_row}'

# STORE WORDS WHICH WILL BE PART OF THE QUESTION, ONE OF THEM IS RIGHT
box = []

# STORE THE MEANING OF THE WORDS
box_translation = []

# CHOSEN NOUN
noun = choice(nouns)

# FIND THE INDEX OF THE CHOSEN NOUN
noun_index = nouns.index(noun)

# GET THE TRANSLATION OF THE CHOSEN NOUN THROUGH ITS INDEX
noun_translation = substantivos[noun_index]

# PLACE THE CORRECT ANSWER INTO A LIST FOR FURTHER CHECKAGE
box_correct_translation = [noun_translation]

# CHOSEN NOUN ADDED AS THE FIRST OF THE LIST
box.append(noun)

# ADDING THE MEANING OF THE CHOSEN NOUN TO THE OTHER LIST
box_translation.append(noun_translation)

print(noun)
print(noun_translation)


# BUT 5 WORDS ARE NEEDED TO MAKE A QUIZ, SO FAR THERE IS ONE, THE RIGHT ANSWER
while len(box) < 5:
    # CREATION OF WRONG ANSWERS
    fake = choice(nouns)
    fake_index = nouns.index(fake)
    fake_translation = substantivos[fake_index]

    # ADDITION OF THE WRONG ANSWERS TO THE QUIZ
    box.append(fake)

    # ADDITION OF THE MEANING OF THE WRONG ANSWERS
    box_translation.append(fake_translation)

    # BUT THE CREATOR CAN STILL HAVE A CHANCE TO REPEAT WORDS, AND THIS HAS TO BE AVOIDED
    check_repeated_data = []

    # THIS LOOP ADDS TO ANOTHER LIST, HOW MANY TIMES EACH DATA HAS REPEATED
    for word in box:
        check_repeated_data.append(box.count(word))

    # IF ALL DATA == 1 MEANS SUCCESS, ELSE, THE QUIZ LIST WILL BE CLEANED UP, AND THE CHOSEN NOUN WILL BE READDED
    for data in check_repeated_data:
        if data != 1:
            box.clear()
            box_translation.clear()
            box.append(noun)
            box_translation.append(noun_translation)

print(box)
print(box_translation)
shuffle(box_translation)

print(welcome('TREINO DE SUBSTANTIVOS', prefix=4, prefix2=7))

label = f"""
{bricks} O QUE É {x[3]}{noun}{x[7]} ? {bricks}
{ident}1 {box_translation[0]}
{ident}2 {box_translation[1]}
{ident}3 {box_translation[2]}
{ident}4 {box_translation[3]}
{ident}5 {box_translation[4]}

Digite de 1 a 5, para fornecer sua resposta
Digite após a seta -> """

answer = int(input(label))

if answer == 1:
    if box_translation[0] in box_correct_translation:
        print(success)
    else:
        print(failure)

elif answer == 2:
    if box_translation[1] in box_correct_translation:
        print(success)
    else:
        print(failure)

elif answer == 3:
    if box_translation[2] in box_correct_translation:
        print(success)
    else:
        print(failure)

elif answer == 4:
    if box_translation[3] in box_correct_translation:
        print(success)
    else:
        print(failure)

elif answer == 5:
    if box_translation[4] in box_correct_translation:
        print(success)
    else:
        print(failure)
