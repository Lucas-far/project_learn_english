

def welcome(algorithm_name: str = 'Name of the algorithm', prefix: int = 0, prefix2: int = 7) -> str:
    """
    To receive a string and return it as the name of the algorithm
    :param algorithm_name:
    :param prefix: goes from 0 to 6, and combine with prefix2, frozen as 7. EX: prefix = 0 & prefix2 = 7 = black
    :param prefix2: must always be 7, if it is desired colors to work
    :return: str
    """
    bricks = '=' * 20
    pallet: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    return f'\n{bricks} Bem-vindo ao {pallet[prefix]}{algorithm_name}{pallet[prefix2]} {bricks}'

if __name__ == '__main__':
    pass
