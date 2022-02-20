"""
Word Class
"""
import random
from syllables import Syllable


class Word:
    """
    Word Class
    """
    def __init__(self, num_syllables, consonants, vowels, part_of_speech):
        self.word = []
        self.part_of_speech = part_of_speech

        self.word.append(Syllable(random.choice(consonants), random.choice(vowels)))

        for i in range(num_syllables - 2):
            new_syl = Syllable(random.choice(consonants), random.choice(vowels))
            self.word.append(new_syl)

        self.word.append(Syllable(random.choice(consonants), random.choice(vowels)))

    def stringify(self):
        new_string = ""

        for i in range(len(self.word)):
            new_string = new_string + self.word[i].stringify()

        return new_string

if __name__ == "__main__":
    random.seed()

    new_word = Word(3)

    print(new_word.stringify())