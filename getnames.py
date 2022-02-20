"""
Word Class
"""
import random
import copy
from words import Word


def make_diphthongs(pool):
    """
    Makes unique pairs out of every combination of vowels.
    """
    new_array = copy.copy(pool)
    for i in range(len(pool)):
        for j in range(len(pool)):
            if i != j:
                diphthong = pool[i] + pool[j]
                new_array.append(diphthong)

    return new_array


def get_name_list(num_words, consonants, vowels):
    """
    Generates a list of names from a random selection of 7 consonants and 5 vowels.
    Returns an array of strings.
    """
    truncated_consonants = random.choices(consonants, k=7)
    truncated_vowels = random.choices(vowels, k=5)

    name_list = []
    duplicate_checker = {}

    for i in range(num_words):
        valid = 0
        generation_attempt_tracker = 0
        while valid == 0:
            generation_attempt_tracker += 1
            new_name = Word(random.randint(1,3), truncated_consonants, truncated_vowels, "name")
            new_name_string = new_name.stringify()

            # Makes sure there aren't any duplicate names.
            if duplicate_checker.get(new_name_string) is None:
                duplicate_checker.update({new_name_string : 1})
                name_list.append(new_name_string)
                valid = 1

            if generation_attempt_tracker == 1000:
                print("ERROR: Too many words requested. Please choose a smaller number.")
                return get_error_list(num_words, message)

    return name_list


def get_error_list(n, message):
    """
    Populates an array with a given message n times.
    """
    error_array = []
    for i in range[n]:
        error_array.append(message)

    return error_array


if __name__ == "__main__":
    random.seed()

    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
                      'x', 'y', 'z', 'ch', 'sh', 'th', 'jh', 'gh', 'tl', 'st', 'sk', 'sp']

    vowel_pool = ['a', 'e', 'i', 'o', 'u']

    vowels = make_diphthongs(vowel_pool)

    vowels.append('oo')

    while True:
        f = open('request.txt')
        lines = f.readlines()
        f.close

        if len(lines) > 0:
            print("Received Request")
            if lines[0].isnumeric():
                name_list = get_name_list(int(lines[0]), consonants, vowels)
            else:
                print("ERROR: Non-number requested.")
                name_list = get_error_list(20, "ERROR: Non-Number Requested")

            f = open('request.txt', 'w')
            f.write("")
            f.close()

            f = open('response.txt', 'w')
            f.truncate()
            contents = ""
            for i in range(len(name_list) - 1):
                contents += name_list[i]
                if i != len(name_list) - 1:
                    contents += '\n'
            f.write(contents)
            f.close()
