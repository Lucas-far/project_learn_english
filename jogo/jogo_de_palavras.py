

from banco_de_dados import *
from cores import colors as x
from random import choice
from traduzir import do_translation as traduza

# ----------------------------------------------------- SUBTANTIVO -----------------------------------------------------
substantivo = choice(nouns)
substantivo_def = traduza(substantivo, 'pt')
substantivo_tupla = f'("{substantivo}", "{substantivo_def}"), '  # dado a ser escrito no arquivo
print(f'Sugira-me um substantivo: {x[4]}{substantivo}{x[7]}')

# -------------------------------------------------------- CAN ---------------------------------------------------------
can = choice(can_could_global)
can_def = traduza(can, 'pt')
can_tupla = f'("{can}", "{can_def}"), '  # dado a ser escrito no arquivo
print(f'Sugira-me uma forma do verbo can: {x[4]}{can}{x[7]}')

# -------------------------------------------------------- HAVE --------------------------------------------------------
have = choice(has_have_gl)
have_def = traduza(have, 'pt')
have_tupla = f'("{have}", "{have_def}"), '  # dado a ser escrito no arquivo
print(f'Sugira-me uma forma do verbo have: {x[4]}{have}{x[7]}')

# ------------------------------------------------------- ARTIGO -------------------------------------------------------
artigo = choice(art_gl)
artigo_def = traduza(artigo, 'pt')
artigo_tupla = f'("{artigo}", "{artigo_def}"), '  # dado a ser escrito no arquivo
print(f'Sugira-me uma forma do verbo have: {x[4]}{artigo}{x[7]}')

with open('bdd.py', 'a') as py:
    py.write(substantivo_tupla)  # adicionar substantivo
    py.write(can_tupla)          # adicionar uma forma do verbo can
    py.write(have_tupla)         # adicionar uma forma do verbo have
    py.write(artigo_tupla)       # adicionar um artigo
