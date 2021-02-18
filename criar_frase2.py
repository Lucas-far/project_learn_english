

from criar_frase import sentence_maker

from gramatica.pronomes import pronouns_personal_upper
from gramatica.verbo_to_be import to_be_present
from gramatica.adjetivos.adjetivos import adjectives
from gramatica.artigos import *
from gramatica.substantivos import nouns
from gramatica.verbos_infinitivo import verbs_infinitive
from gramatica.tempo_verbal_present import present_time_tense
from gramatica.adjetivos_possessivos import adjectives_possessive


# Método para frases de 3 elementos
def sentence_joiner_three_elements(first_database, second_database, third_database, database_len):
    """"""
    joiner = []
    counter = 0
    while counter < len(database_len):
        joiner.append(first_database[0] + ' ' + second_database[0] + ' ' + third_database[counter])
        joiner.append(first_database[1] + ' ' + second_database[1] + ' ' + third_database[counter])
        joiner.append(first_database[2] + ' ' + second_database[1] + ' ' + third_database[counter])
        joiner.append(first_database[3] + ' ' + second_database[1] + ' ' + third_database[counter])
        joiner.append(first_database[4] + ' ' + second_database[2] + ' ' + third_database[counter])
        joiner.append(first_database[5] + ' ' + second_database[2] + ' ' + third_database[counter])
        joiner.append(first_database[6] + ' ' + second_database[2] + ' ' + third_database[counter])

        counter += 1

    # print(len(joiner))
    return joiner





if __name__ == '__main__':
    sentence_with_three_elements = sentence_joiner_three_elements(
        first_database=pronouns_personal_upper,
        second_database=to_be_present,
        third_database=adjectives,
        database_len=adjectives
    )
    print(sentence_with_three_elements)
