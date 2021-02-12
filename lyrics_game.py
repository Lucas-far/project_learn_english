

"""

"""

from random import choice
from traduzir import do_translation

lyrics = """
You love me,
What would you say,
What can you do,
I feel so strong,
I feel brand new,
And I can give my all to you,
I wanna feel emotion,
I wanna wrap you in my arms,
And never leave you lonely,
Forever stay here by your side,
You show me,
You love me,
You show me how to breakaway,
Living in a brand new day,
You wake me up,
You change me,
You keep on lighting the way,
You show me love,
You show me how to break away,
Living in a brand new day""".split(',')

lyrics = [index.replace(index[:1], '') for index in lyrics]

print(lyrics)

var = choice(lyrics)

print(f"{var} -> {do_translation(var, 'pt')}")
