

from gramatica.adjetivo import adjectives
from metodos.banco_de_dados import verify


the_adjectives = adjectives
# verify('insira o adjectivo aqui', database=the_adjectives)

"------------------------------------------------ PROCURANDO DADO -------------------------------------------------"
#       parâmetro 1 = strings                , parâmetro 2 = variável
verify('small', 'big', 'weird', 'fast', '...', database=the_adjectives)    # EXEMPLO DE PROCURA DE 5 DADOS

"verify('small', 'big', 'weird', '...', database=the_adjectives)"  # EXEMPLO DE PROCURA DE 4 DADOS
"verify('small', 'big', '...', database=the_adjectives)"           # EXEMPLO DE PROCURA DE 3 DADOS
"verify('small', '...', database=the_adjectives)"                  # EXEMPLO DE PROCURA DE 2 DADOS
"verify('small', database=the_adjectives)"                         # EXEMPLO DE PROCURA DE 1 DADOS

"----------------------------------------- SINTAXE PARA ADICIONAR STRING ------------------------------------------"
"aspas + palavra + aspas + vírgula + espaço"  # 'palavra', 'palavra2', 'palavra3', ...
