

from textblob import TextBlob
from banco_de_dados import nouns
from random import choice

def do_translation(text, target_language):
    """"""
    sentence_translated = TextBlob(text).translate(to=target_language)
    return sentence_translated

if __name__ == '__main__':
    print(do_translation(text=choice(nouns), target_language='pt'))

    # Basta escrever um texto onde diz "escrever o texto aqui", e onde
    print(do_translation('escrever o texto aqui', 'pt'))
