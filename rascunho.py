

"""
I have a tv to watch    -> Eu tenho uma tv para assistir (infinitivo)
I watch tv              -> Eu assisto TV                 (presente)
I am watching tv        -> Estou assistindo tv           (presente contínuo)
I have watched tv       -> Eu assisti tv                 (presente perfeito)
I have been watching tv -> Eu tenho assistido tv         (presente perfeito contínuo)

I watched tv            -> Eu assisti TV                  (passado)
I was watching tv       -> Eu estava assistindo televisão (passado contínuo)
I had watched tv        -> Eu tinha assistido tv          (passado perfeito)
I had been watching tv  -> Eu estava assistindo tv        (passado perfeito contínuo)

I will watch tv              -> Vou assistir tv           (futuro)
I will be watching tv        -> Estarei assistindo tv     (futuro contínuo)
I will have watched tv       -> Eu terei assistido tv     (futuro perfeito)
I will have been watching tv -> Eu estarei assistindo tv  (fututro perfeito contínuo)
"""

from gramatica.substantivos.substantivos import nouns_dict, nouns_dict_keys
from random import choice

this_key = choice(nouns_dict_keys)
this_key_values = nouns_dict[this_key]  # the values

print(this_key)
print(this_key_values)
print(this_key_values[0])
print(this_key_values[1])
print(this_key_values[2])
print(this_key_values[3])
