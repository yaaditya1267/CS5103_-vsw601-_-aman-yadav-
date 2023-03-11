CS5103 Software Engineering : Course Project
--------------------------------------------
Aman Kumar Yadav, VSW601
------------------------
Professor: Xiaoyin Wang
-----------------------
Checkpoint: 3/10/2023
----------------------
Language:Python3
-------------------------------------------------------------------------------------------------------


PROJECT DESCRIPTION:
-------------------

Strings and Words: In this project I are writing a program to perform various word statistics of a given document (as a string). The initial requirement is to count the frequency of each unique word. The code should support combinations of space, tab, and newline characters as separators.



TEST CASE 1
-----------
TEST CASE DESCRIPTION
---------------------

In this following unit test you need to enter a string that basically returns the count/frequency of each unique words and it can also read across spaces,tabs and newline character as seperator.

TEST DATA

Input String: once upon a time aman was  playing football and was cricket

EXPECTED RESULTS

Output: 'once': 1, 'upon': 1, 'a': 1, 'time': 1, 'aman': 1, 'was': 2, 'playing': 1, 'football': 1, 'and': 1, 'cricket': 1
-------------------------------------------------------------------------------------------------------
TEST CASE 2
-----------
TEST CASE DESCRIPTION
---------------------


In this following unit test you need to enter a string that basically returns the count/frequency of each unique character and it can also read across spaces,tabs and newline character as seperator.

TEST DATA

Input String: once upon a Time aman was Playing football and was cricket

EXPECTED RESULTS

Output: 'a': 8, 'b': 1, 'c': 3, 'd': 1, 'e': 3, 'f': 1, 'g': 1, 'i': 3,'P':1,'T':1, 'k': 1, 'l': 3, 'm': 2, 'n': 5, 'o': 4, 'p': 1, 'r': 1, 's': 2, 't':2 , 'u': 1, 'w': 2, 'y': 1,' ': 10
-------------------------------------------------------------------------------------------------------
TEST CASE 3
-----------
TEST CASE DESCRIPTION
---------------------

In this following test you need to enter a string that basically returns the count/frequency of uppercase character present in the input.

TEST DATA

Input String: once upon a Time aman was Playing football and was cricket

EXPECTED RESULTS

Output: 2
-------------------------------------------------------------------------------------------------------
TEST CASE 4
-----------
TEST CASE DESCRIPTION
---------------------


In this following unit test you need to enter a string that basically returns the new .txt file by converting all lowercase character into uppercase.

TEST DATA

Input String: once upon a time 

EXPECTED RESULTS

Output: ONCE UPON A TIME 
--------------------------------------------------------------------------------------------------------
How to run program on Terminal :-

Please make sure Python3 is installed before you start.

Change directory to where 'main.py' is located. 
Enter 'python3 main.py' on terminal to run python file.
The program will execute and will print the output accordingly to the text taken as input. 
It prints the count of unique words.

And  I have also performed bug detection using PYLINT.
--------------------------------------------------------------------------------------------------------

