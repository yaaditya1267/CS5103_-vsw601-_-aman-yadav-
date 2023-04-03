"""
Created by: Aman kumar yadav(vsw601)
"""
import unittest
from main import count_word_number, count_char_number, count_uppercase, count_lines_and_characters, merge_input

class wd_count(unittest.TestCase):
    def test_count_word(self):
        with open('input.txt', 'r') as f:
            document = f.read()
        output = {'once': 1, 'upon': 1, 'a': 1, 'time': 1, 'aman': 1, 'was': 2, 'playing': 1, 'football': 1, 'and': 1, 'cricket': 1}
        self.assertEqual(count_word_number(document), output)

    def test_count_char(self):
        with open('input1.txt', 'r') as f:
            document = f.read()
        output = {'a': 8, 'b': 1, 'c': 3, 'd': 1, 'e': 3, 'f': 1, 'g': 1, 'i': 3,'P':1,'T':1, 'k': 1, 'l': 3, 'm': 2, 'n': 5, 'o': 4, 'p': 1, 'r': 1, 's': 2, 't':2 , 'u': 1, 'w': 2, 'y': 1,' ': 10}
        self.assertEqual(count_char_number('input1.txt'), output)
    

    def test_count_uppercase(self):
        input_file = 'input1.txt'
        output = 2
        with open(input_file, 'w') as f:
            f.write('once upon a Time aman was Playing football and was cricket')
        self.assertEqual(count_uppercase(input_file), output)
    

    def test_convert_to_uppercase(self):
        with open("input2.txt", "r") as f:
            input_text = f.read()
        output_text = input_text.upper()
        with open("output_uppercase.txt", "w") as f:
            f.write(output_text)
        with open("output_uppercase.txt", "r") as f:
            output_file_contents = f.read()
        self.assertEqual(output_file_contents, "ONCE UPON A TIME ")
    
    def test_count_lines_and_characters(self):
        num_lines, num_chars = count_lines_and_characters()
        self.assertEqual(num_lines, 3)
        self.assertEqual(num_chars, 15)

    def test_merge_input(self):
        with open('input7.txt', 'r') as file:
            input_str = file.read()
        expected = "(Helloeveryone)"
        self.assertEqual(merge_input(input_str), expected)

    
    def test_replace_chars(self):
        with open('input8.txt', 'r') as input_file:
            input_str = input_file.read()
        expected = 'Hello everyone'
        output_str = input_str.replace('t', 'e').strip()
        with open('output3.txt', 'w') as output_file:
            output_file.write(output_str)
        with open('output3.txt', 'r') as output_file:
            output_str = output_file.read().strip()
        self.assertEqual(output_str, expected)


    
if __name__ == '__main__':
    unittest.main()
