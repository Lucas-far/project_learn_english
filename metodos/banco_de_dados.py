

def get_input_int(the_input: int = 1, text: str = 'Write an integer -> ', start: int = 1, limit: int = 9999) -> int:
    """
    To treat improper data while a proper integer number is not being provided.
    :param the_input:
    :param text:
    :param start:
    :param limit:
    :return: int
    """

    pallet: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    red, paint = pallet[1], pallet[7]
    error_label = '==================== ERRO ===================='
    delimiter = '=' * len(error_label)

    integer_out_of_range = f"""
        {red}{error_label}{paint}
        As opções são números entre {start} até {limit} :)
        {red}{delimiter}{paint}"""

    integer_unused = f"""
        {red}{error_label}{paint}
        Você não está usando números. Use números entre {start} até {limit} :)
        {red}{delimiter}{paint}"""

    while the_input <= start or the_input > limit:
        try:
            the_input = int(input(text))
            if the_input in range(start, limit + 1):
                break
            else:
                print(integer_out_of_range)
        except ValueError:
            print(integer_unused)

    return the_input


def message_frame(the_message: str = f'----- MENSAGEM -----') -> str:
    """"""
    return the_message


def welcome(algorithm_name: str = 'Name of the algorithm', prefix: int = 0, prefix2: int = 7) -> str:
    """
    To receive a string and return it as the name of the algorithm

    :param algorithm_name:
    :param prefix: goes from 0 to 6, and combine with prefix2, frozen as 7. EX: prefix = 0 & prefix2 = 7 = black
    :param prefix2: must always be 7, if it is desired colors to work
    :return: str
    """

    bricks = '=' * 50

    pallet: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    return f"""
        {bricks}
        Bem-vindo ao {pallet[prefix]}{algorithm_name.upper()}{pallet[prefix2]}
        {bricks}"""

if __name__ == '__main__':
    print(welcome('treino de substantivo', prefix=3, prefix2=7))
