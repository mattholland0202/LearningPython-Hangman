hangman0 = r""

hangman1 = r"""





_ _ _ _
"""

hangman2 = r"""

   |
   |
   |
   |
_ _|_ _
"""

hangman3 = r"""
    _ _ _ _
   |
   |
   |
   |
_ _|_ _
"""

hangman4 = r"""
    _ _ _ _
   |       |
   |
   |
   |
_ _|_ _
"""

hangman5 = r"""
    _ _ _ _
   |       |
   |       0
   |
   |
_ _|_ _
"""

hangman6 = r"""
    _ _ _ _
   |       |
   |       0
   |       |
   |
_ _|_ _
"""

hangman7 = r"""
    _ _ _ _
   |       |
   |       O
   |      /|
   |
_ _|_ _
"""

hangman8 = r"""
    _ _ _ _
   |       |
   |       O
   |      /|\
   |
_ _|_ _
"""

hangman9 = r"""
    _ _ _ _
   |       |
   |       O
   |      /|\
   |      /
_ _|_ _
"""

hangman10 = r"""
    _ _ _ _
   |       |
   |       O
   |      /|\
   |      / \
_ _|_ _
"""

hangmen = [hangman0, hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman7, hangman8, hangman9, hangman10]


def print_hangman(value):
    return hangmen[value]