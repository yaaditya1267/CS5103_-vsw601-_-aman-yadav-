"""
Created by: Aman kumar yadav(vsw601)
"""
import string


def count_uppercase_letters(filename):
    """
    It returns the number of uppercase letters in a given file.
    It returns Number of uppercase letters.
    """
    with open(filename, "r", encoding="utf-8") as file:
        document = file.read()
        count = 0
        for char in document:
            if char.isupper():
                count += 1
        return count


def count_char_number(filename):
    """
    It returns the frequency of each character in the given file.
    It returns dictionary with character count.
    """
    # Open and read the file
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # Create an empty dictionary to store the counts
    char_count = {}
    # Loop through each character in the text
    for char in text:
        # Check if the character is a printable ASCII character
        if char in string.printable:
            # Check if the character is already in the dictionary
            if char in char_count:
                # If so, increment the count by 1
                char_count[char] += 1
            else:
                # If not, add the character to the dictionary with a count of 1
                char_count[char] = 1
    # Return the dictionary of character counts
    return char_count




def count_word_number(text):
    """
    It returns the frequency of each unique word in the document variable.
    It returns dictionary with word counts
    """
    # It converts text to lowercase and replace tabs and newlines with spaces.
    text = text.lower().replace('\t', ' ').replace('\n', ' ')

    # It splits text into words using spaces as separators.
    words = text.split(' ')

    # It initializes an empty dictionary to store the word count.
    freq_dict = {}

    # It iterates over each word and update the frequency count in the dictionary.
    for word in words:
        if word != '':
            freq_dict[word] = freq_dict.get(word, 0) + 1

    #It returns the dictionary of count_word.
    return freq_dict


if __name__ == '__main__':
    # It reads the text from the input file.
    with open('input.txt', 'r', encoding='utf-8') as f:
        document = f.read()

    # It counts the number of uppercase letters, characters, and words.
    UPPERCASE_COUNT = count_uppercase_letters('input1.txt')
    CHAR_COUNT = count_char_number('input1.txt')
    WORD_COUNT = count_word_number(document)

    # It print the count for each unique word.
    print(f"{'Word':<15}{'Frequency'}")
    print("-" * 25)
    for w_ord, freq in WORD_COUNT.items():
        print(f"{w_ord:<15}{freq}")
    print("\n")
