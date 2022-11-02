"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""


# Using Counter elements are converted to Dictionary keys
# and their count as Dictionary value or frequency.
from collections import Counter


def generate_phrase(characters, phrase):
    characters_count = Counter(characters.lower())
    phrase_count = Counter(phrase.lower())
    return all(characters_count.get(character, 0) >= count for character, count in phrase_count.items())


# Test cases
print(generate_phrase('cbacba', 'aabbccc'))  # False

print(generate_phrase('miirrree', 'mirror'))  # False

print(generate_phrase('', ''))  # True

print(generate_phrase('pyprogthramon3', 'Python3'))  # True

print(generate_phrase("hellsdo wo rdld!", "hello world!"))   # True

