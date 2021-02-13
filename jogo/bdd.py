

bdd = []

def look_for_word(the_word):
    """"""
    colors: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )
    success = """
    {}
    ==================================================== RESULTADO =====================================================
    {}
    Palavra procurada: {}
    Resultado: {}{}{}                                                                                                 
    {}
    ====================================================================================================================
    {}
    """

    failure = f"""
    {colors[1]}
    ==================================================== RESULTADO =====================================================
    {colors[7]}
    Dado não encontrao
    {colors[1]}
    ====================================================================================================================
    {colors[7]}
    """

    counter = 0
    while counter < len(bdd):
        if the_word == bdd[counter][0]:
            print(success.format(
                colors[3], colors[7], the_word, colors[4], bdd[counter], colors[7], colors[3], colors[7]))
            break
        else:
            counter += 1
            if counter >= len(bdd):
                print(failure)


def recycle_database():
    """"""
    global bdd
    bdd = list(set(bdd))
    return f'{bdd = }'


if __name__ == '__main__':
    look_for_word('')
    print(recycle_database())

""  # Pegar a nova palavra criada e recortá-la para dentro do dicionário
""  # executar esse arquivo [ bdd.py ], copiar o retorno [ shift + down ]
""  # copiar o retorno, e substituir a variável [ bdd ] acima

("cities", "cidades"), ("Could not", "Não poderia"), ("Has not", "Não tem"), ("an", "a"), 