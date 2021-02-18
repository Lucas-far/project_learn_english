

from gramatica.substantivos.substantivos import nouns_dict, nouns_dict_keys
from gramatica.adjetivos.adjetivos import adjectives_dict, adjectives_dict_keys
from gramatica.adverbios.adverbios import adv_ly_dict, adv_ly_dict_keys
from gramatica.verbos.verbos_infinitivo import verbs_inf_dict, verbs_inf_dict_keys
from gramatica.verbos.verbos_presente_sgl import pst_sgl_dict, pst_sgl_dict_keys
from gramatica.verbos.verbos_presente_pl import pst_pl_dict, pst_pl_dict_keys
from gramatica.verbos.verbos_passado import past_dict, past_dict_keys
from gramatica.verbos.verbos_futuro import fut_dict, fut_dict_keys

if __name__ == '__main__':
    "-------------------------------------------------- SUBSTANTIVOS --------------------------------------------------"
    print('\n')
    print(f'{len(nouns_dict) = }')
    print(f'{len(nouns_dict_keys) = }')
    print(nouns_dict_keys)
    print('\n')

    "--------------------------------------------------- ADJETIVOS ----------------------------------------------------"
    print('\n')
    print(f'{len(adjectives_dict) = }')
    print(f'{len(adjectives_dict_keys) = }')
    print(adjectives_dict_keys)
    print('\n')

    "--------------------------------------------------- ADVÉRBIOS ----------------------------------------------------"
    print('\n')
    print(f'{len(adv_ly_dict) = }')
    print(f'{len(adv_ly_dict_keys) = }')
    print(adv_ly_dict_keys)
    print('\n')

    "--------------------------------------------------- INFINITIVO ---------------------------------------------------"
    print('\n')
    print(f'{len(verbs_inf_dict) = }')
    print(f'{len(verbs_inf_dict_keys) = }')
    print(verbs_inf_dict_keys)
    print('\n')

    "-------------------------------------------- PRESENT SIMPLE SINGULAR ---------------------------------------------"
    print('\n')
    print(f'{len(pst_sgl_dict) = }')
    print(f'{len(pst_sgl_dict_keys) = }')
    print(pst_sgl_dict_keys)
    print('\n')

    "--------------------------------------------- PRESENT SIMPLE PLURAL ----------------------------------------------"
    print('\n')
    print(f'{len(pst_pl_dict) = }')
    print(f'{len(pst_pl_dict_keys) = }')
    print(pst_pl_dict_keys)
    print('\n')

    "-------------------------------------------------- PAST SIMPLE ---------------------------------------------------"
    print('\n')
    print(f'{len(past_dict) = }')
    print(f'{len(past_dict_keys) = }')
    print(past_dict_keys)
    print('\n')

    "------------------------------------------------- FUTURE SIMPLE --------------------------------------------------"
    print('\n')
    print(f'{len(fut_dict) = }')
    print(f'{len(fut_dict_keys) = }')
    print(fut_dict_keys)
    print('\n')
