

from gramatica.substantivo import nouns
from metodos.banco_de_dados import verify


the_nouns = nouns
# print(verify('insira substantivo aqui', database=the_nouns))

"------------------------------------------------ PROCURANDO DADO -------------------------------------------------"
#       parâmetro 1 = strings                , parâmetro 2 = variável
print(verify('castle', 'person', 'elephant', 'sidewalk', '...', database=the_nouns))  # EXEMPLO DE PROCURA DE 5 DADOS

"verify('small', 'big', 'weird', '...', database=the_nouns)"  # EXEMPLO DE PROCURA DE 4 DADOS
"verify('small', 'big', '...', database=the_nouns)"           # EXEMPLO DE PROCURA DE 3 DADOS
"verify('small', '...', database=the_nouns)"                  # EXEMPLO DE PROCURA DE 2 DADOS
"verify('small', database=the_nouns)"                         # EXEMPLO DE PROCURA DE 1 DADOS

"----------------------------------------- SINTAXE PARA ADICIONAR STRING ------------------------------------------"
"aspas + palavra + aspas + vírgula + espaço"  # 'palavra', 'palavra2', 'palavra3', ...
