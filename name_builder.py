"""
Word Class
"""
import random
import copy
from words import Word


def make_diphthongs(pool):
    new_array = copy.copy(pool)
    for i in range(len(pool)):
        for j in range(len(pool)):
            diphthong = pool[i] + pool[j]
            new_array.append(diphthong)

    return new_array


def reduce_phoneme_pool(phonemes, number_of_phonemes):
    reduced_phoneme_list =
    return reduced_phoneme_list


def get_name_list(num_words, consonants, vowels):
    pass

if __name__ == "__main__":
    random.seed()

    consonant_pool = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
                      'x', 'y', 'z', 'ch', 'sh', 'th', 'jh', 'gh']

    single_vowel_pool = ['a', 'e', 'i', 'o', 'u']

    vowel_pool = make_diphthongs(single_vowel_pool)

    reduced_consonants = random.choices(consonant_pool, k=7)
    reduced_vowels = random.choices(vowel_pool, k=7)

    while