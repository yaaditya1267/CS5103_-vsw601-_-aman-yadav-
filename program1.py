
"""
Created by: Aman kumar yadav (vsw601)
"""
import re
from collections import Counter

def count_words(text):
    """
    It basically count the number of occurrences of each word in the given text.
    return: word_counts_func
    """
    words = re.findall(r'\b\w+\b', text)
    word_counts_func = Counter(words)
    return word_counts_func

def count_characters(text):
    """
    It basically count the number of occurrences of each character in the given text.
    return: character_counts_func
    """
    characters = re.findall(r'\S', text)
    character_counts_func = Counter(characters)
    return character_counts_func

def count_spaces(text):

    """
    It basically count the number of occurrences of each space in the given text.
    return: space_counts_func
    """
    spaces = re.findall(r'[ \t]+', text)
    space_counts_func = Counter(spaces)
    return space_counts_func

def count_punctuation(text):

    """
    It basically count the number of occurrences of each punctuation in the given text.
    return: punctuation_counts_func
    """
    punctuation = re.findall(r'[^\w\s]+', text)
    punctuation_counts_func = Counter(punctuation)
    return punctuation_counts_func

if __name__ == '__main__':
    text_input = input('Enter text: ')

    word_counts = count_words(text_input)
    character_counts = count_characters(text_input)
    space_counts = count_spaces(text_input)
    punctuation_counts = count_punctuation(text_input)

    print("*" * 120)
    print('TOTAL WORD COUNTS--->', dict(word_counts))
    print('TOTAL CHARACTER COUNTS--->', dict(character_counts))
    print('TOTAL SPACE COUNTS--->', dict(space_counts))
    print('TOTAL PUNCTUATION COUNTS--->', dict(punctuation_counts))
    print("*" * 120)
