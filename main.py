"""
Created by: Aman kumar yadav(vsw601)
"""
import re
import string


def merge_input(input_str):
    """
    It merges the input into one line.
    """
    lines = [line.strip() for line in input_str.split('\n')]
    # It removes any empty lines from the list
    lines = [line for line in lines if line]
    merged = ''.join(lines)
    merged = merged.capitalize()
    # It adds a space between the merged words
    merged = ' '.join(merged.split())
    return f"({merged})"

def replace_word(text, pattern, replacement):
    """
    It replaces the word.
    """
    pattern = rf'\b{re.escape(pattern)}\b'
    return re.sub(pattern, replacement, text, flags=re.IGNORECASE)

text = "Once upon a time someone came Once"
pattern = "Once"
replacement = "Twice"
new_text = replace_word(text, pattern, replacement)


def replace_word_in_first(text, pattern, replacement):
    """
    It replaces the word in first line only
    """
    # It splits the text into lines
    lines = text.split("\n")
    # It replaces the pattern with the replacement in the first line
    lines[0] = lines[0].replace(pattern, replacement)
    # It joins the lines back together
    return "\n".join(lines)

def count_lines_and_characters():
    """
    It counts the number of line and number of character present.
    """
    with open("input6.txt", "r", encoding="utf-8") as file:
        text = file.read()
    lines = text.split('\n')
    num_lines = len(lines)
    num_chars = len(text)
    return num_lines, num_chars



def convert_to_uppercase():
    """
    It converts all the lowercase word to uppercase.
    """
    with open("input2.txt", "r", encoding="utf-8") as file:
        input_text = file.read()

    # It converts to uppercase
    output_text = input_text.upper()

    # It writes output to file called output_uppercase.txt
    with open("output_uppercase.txt", "w", encoding="utf-8") as file:
        file.write(output_text.rstrip())

    # It returns output
    return output_text



def count_uppercase(filename):
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



def count_lines(text):
    """
    It counts the number of lines.
    """
    lines = text.split('\n')
    return len(lines)


def count_characters(text):
    """
    It counts the number of character.
    """
    characters = 0
    for char in text:
        if char not in (' ','\n'):
            characters += 1
    return characters

# Read input from file
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()


def count_char_number(filename):
    """
    It returns the frequency of each character in the given file.
    It returns dictionary with character count.
    """
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # It creates an empty dictionary to store the counts
    char_count = {}
    for char in text:
        # It checks if the character is a printable character
        if char in string.printable:
            # It checks if the character is already in the dictionary
            if char in char_count:
                # It basically increment the count by 1
                char_count[char] += 1
            else:
                char_count[char] = 1
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
    # It basically reads the text from the input file.
    with open('input.txt', 'r', encoding='utf-8') as f:
        document = f.read()

    # It counts the number of uppercase letters, characters, and words.
    UPPERCASE_COUNT = count_uppercase('input1.txt')
    CHAR_COUNT = count_char_number('input1.txt')
    WORD_COUNT = count_word_number(document)
    line_count = count_lines(text)
    char_count = count_characters(text)

    # It prints the count for each unique word.
    print("-" * 25)
    print("Text: Once upon a time someone came Once\nPattern: Once\nReplacement: Twice\n")
    print(f"Final Output: {new_text}")
    print("-" * 25)
    print(f"Number of lines: {line_count}")
    print("-" * 25)
    print(f"Number of characters: {char_count}")
    print("-" * 25)
    print(f"{'Word':<15}{'Frequency'}")
    print("-" * 25)
    for w_ord, freq in WORD_COUNT.items():
        print(f"{w_ord:<15}{freq}")
    print("-" * 25)
