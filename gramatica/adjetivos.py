

adjectives = [
    'other', 'new', 'good', 'high', 'old', 'great', 'big', 'American', 'small', 'large', 'national', 'young',
    'different', 'black', 'long', 'little', 'important', 'political', 'bad', 'white',

    'real', 'best', 'right', 'social', 'only', 'public', 'sure', 'low', 'early', 'able', 'human', 'local', 'late',
    'hard', 'major', 'better', 'economic', 'strong', 'possible', 'whole',

    'free', 'military', 'true', 'federal', 'international', 'full', 'special', 'easy', 'clear', 'recent', 'certain',
    'personal', 'open', 'red', 'difficult', 'available', 'likely', 'short', 'single', 'medical',

    'current', 'wrong', 'private', 'past', 'foreign', 'fine', 'common', 'poor', 'natural', 'significant',
    'similar', 'hot', 'dead', 'central', 'happy', 'serious', 'ready', 'simple', 'left', 'physical',

    'general', 'environmental', 'financial', 'blue', 'democratic', 'dark', 'various', 'entire', 'close', 'legal',
    'religious', 'cold', 'final', 'main', 'green', 'nice', 'huge', 'popular', 'traditional', 'cultural',

    'stupid', 'irrelevant', 'sweet', 'angry', 'ambitious', 'indifferent', 'marvelous', 'identical', 'clever',
    'enthusiastic', 'vibrant', 'affirmative', 'negative', 'comprehensive', 'intuitive', 'strange', 'weird', 'odd',
    'worthy', 'flexible'
]

""  # skip a row and add 20 new adjectives
""  # for each one, use [ ctrl + shift + <- ] and then [ ctrl + alt + shift + j ] to see if the word is repeated
""  # write down all words in string format, copy all of them, go to translator, and paste them (spelling accuracy)
""  # if everything is correct, go back to this file
""  # now select the start of each added word, and after selecting all of them, write down [ the + ' ' ]
""  # copy the content and paste it into the [ adjectives2.py ] file
""  # come back to [ adjectives.py ] and undo the changes, and rearrange the new words in the list
""  # check out if both files [ adjectives.py ] and [ adjectives2.py ] have the same length

if __name__ == '__main__':
    print(len(adjectives))
    print(adjectives[20 - 1])
    print(adjectives[40 - 1])
    print(adjectives[60 - 1])
    print(adjectives[80 - 1])
    print(adjectives[100 - 1])
