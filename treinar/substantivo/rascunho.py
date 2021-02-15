
from gramatica.substantivo import nouns, substantivos
from metodos.metodos import *
from random import choice, shuffle
from cores import colors

# CONTENT HIGHLIGHT AND SPLIT
red, purple, yellow, blue, paint = colors[1], colors[2], colors[3], colors[4], colors[7]
break_row = '\n'
indent = '    '
bricks = '=' * 20
report_model = '==================== RELATÓRIO ===================='
splitter = '=' * len(report_model)

# VARIABLES TO DETERMINE THE PLAYER'S EFFICACY
positive_score = 0
negative_score = 0


while True:

    "STEP 1"  # CREATING THE MAIN WORD, ITS TRANSLATION, AND LISTS WHICH WILL MANAGE THINGS

    box = []                                      # STORE WORDS FOR THE QUIZ
    box_translation = []                          # STORE THE MEANING OF THE WORDS
    noun = choice(nouns)                          # CHOSEN NOUN
    noun_index = nouns.index(noun)                # FIND THE INDEX OF THE CHOSEN NOUN
    noun_translation = substantivos[noun_index]   # GET THE TRANSLATION OF THE CHOSEN NOUN
    box_correct_translation = [noun_translation]  # MEANING OF THE CHOSEN NOUN ADDED SEPARATELY
    box_translation.append(noun_translation)      # MEANING OF THE CHOSEN NOUN ADDED AS THE FIRST INDEX OF ANOTHER LIST
    box.append(noun)                              # CHOSEN NOUN ADDED AS THE FIRST INDEX OF THE LIST

    "STEP 2"  # CREATING THE REMAINING WORDS TO FILL THE QUIZ

    while len(box) < 5:  # 4 OTHER WORDS ARE NEEDED TO MAKE A QUIZ, SO FAR THERE IS ONE: THE RIGHT ANSWER

        # CREATION
        fake = choice(nouns)
        fake_index = nouns.index(fake)
        fake_translation = substantivos[fake_index]

        # INSERTION
        box.append(fake)
        box_translation.append(fake_translation)

        "OBS"  # WHILE INSERTING NEW WORDS, THERE IS A CHANCE TO REPEAT WORDS, AND THIS HAS TO BE AVOIDED
        check_repeated_data = []

        # THIS LOOP WILL CHECK HOW MANY TIMES EACH DATA HAS REPEATED
        for word in box:
            check_repeated_data.append(box.count(word))

        # IF ALL DATA == 1 MEANS SUCCESS, ELSE, THE QUIZ LIST WILL BE CLEANED UP, AND THE CHOSEN NOUN WILL BE READDED
        for data in check_repeated_data:
            if data != 1:
                box.clear()
                box_translation.clear()
                box.append(noun)
                box_translation.append(noun_translation)

    "STEP 3"  # RUN ALGORITHM

    shuffle(box_translation)  # AFTER ALL WORDS ARE READY, IT IS STRATEGIC TO SHUFFLE THE LIST

    greetings = welcome('treino de substantivo', prefix=3, prefix2=7)
    print(indent, greetings)

    answer = get_input_int(
        text=f"""
        {bricks} 
        O QUE É {yellow}{noun}{paint} ? 
        {bricks}
        1 - {box_translation[0]}
        2 - {box_translation[1]}
        3 - {box_translation[2]}
        4 - {box_translation[3]}
        5 - {box_translation[4]}

        Digite de 1 a 5, para fornecer sua resposta
        Digite após a seta -> """,
        start=1,
        limit=5
    )

    # label = f"""
    # {bricks}
    # O QUE É {yellow}{noun}{paint} ?
    # {bricks}
    # 1 - {box_translation[0]}
    # 2 - {box_translation[1]}
    # 3 - {box_translation[2]}
    # 4 - {box_translation[3]}
    # 5 - {box_translation[4]}
    #
    # Digite de 1 a 5, para fornecer sua resposta
    # Digite após a seta -> """
    #
    # answer = int(input(label))

    # ONE OF THEM IS CORRECT, THE ONLY CORRECT WILL RETURN A NUMBER LESSER THAN 10

    conditions = [
        *[0 if box_translation[0] in box_correct_translation else 10],
        *[1 if box_translation[1] in box_correct_translation else 11],
        *[2 if box_translation[2] in box_correct_translation else 12],
        *[3 if box_translation[3] in box_correct_translation else 13],
        *[4 if box_translation[4] in box_correct_translation else 14],
    ]

    # THE ONLY NUMBER LESSER THAN 10 IS PLACED AS INDEX 0, AND HAS TO BE +1 BECAUSE THE GAME OPTIONS START AT 1
    correct_answer_index = sorted(conditions)[0] + 1

    success = f"""
        {report_model}
        {blue}Resposta correta{paint}"""

    failure = f"""
        {report_model}
        {red}Resposta incorreta{paint} 
        {blue}Resposta correta:{paint} {box_correct_translation[0]}"""

    games_played = "        \033[1:32mJogos jogados:\033[m {}"

    score_table = "        \033[1:33mPlacar:\033[m \033[1:34mAcertos\033[m {} x {} \033[1:31mErros\033[m"

    if answer == correct_answer_index:
        positive_score += 1
        print(success)
        print(games_played.format(positive_score + negative_score))
        print(score_table.format(positive_score, negative_score))
        print(indent + indent + splitter)
    else:
        negative_score += 1
        print(failure)
        print(games_played.format(positive_score + negative_score))
        print(score_table.format(positive_score, negative_score))
        print(indent + indent + splitter)

    "ALTERNATIVE"
    # if answer == 1:
    #     if box_translation[0] in box_correct_translation:
    #         print(success)
    #     else:
    #         print(failure)
    #
    # elif answer == 2:
    #     if box_translation[1] in box_correct_translation:
    #         print(success)
    #     else:
    #         print(failure)
    #
    # elif answer == 3:
    #     if box_translation[2] in box_correct_translation:
    #         print(success)
    #     else:
    #         print(failure)
    #
    # elif answer == 4:
    #     if box_translation[3] in box_correct_translation:
    #         print(success)
    #     else:
    #         print(failure)
    #
    # elif answer == 5:
    #     if box_translation[4] in box_correct_translation:
    #         print(success)
    #     else:
    #         print(failure)
