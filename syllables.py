# Name: Ansen D. Garvin
# OSU Email: garvina@oregonstate.edu
# Description: Implementation for a Language class.
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
