# Alex wrote a program that reads a number and a word
# from the input to create phrases like "3 cats" and "1 dog".
# Unfortunately, the condition for plural nouns is currently missing.
# Alex doesn't know how to use if statements, but you do. Help Alex complete this program.
# The plural form of a word generally ends with s. 
# All numbers, apart from 1, expect the plural form after them, even zero: "0 birds".
# Words that form their plural not by adding s, will NOT appear in the tests.
number = int(input())
word = input()
add_s = "s"

if number != 1:
    word += add_s

print(number, word)
