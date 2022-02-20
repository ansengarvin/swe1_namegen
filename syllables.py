"""
Syllable class definition file for a language generation program.
"""
import random


class Syllable:
    """
    Syllable class
    """
    def __init__(self, front_char="",  vowel_char="", back_char=""):
        self.front = front_char
        self.vowel = vowel_char
        self.back = back_char

    def stringify(self):
        new_string = self.front + self.vowel + self.back
        return new_string
