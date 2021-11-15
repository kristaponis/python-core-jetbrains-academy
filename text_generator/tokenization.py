from nltk.tokenize import regexp_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# There is a sentence in the input.
# Use the pattern "[A-z'-]+" to print the tokens.
text = input()

print(regexp_tokenize(text, "[A-z'-]+"))


# There is a sentence and also a number in the input.
# You need to create a pattern that extracts only words from the sentence,
# that is, your resulting list should contain neither punctuation marks nor numbers.
# After that, use the index (the second line in the input) and
# print a token from the list of tokens.
# Sample Input:
# > We were on the Queen Elizabeth, coming back from our first trip to Europe.
# > -1
# Sample Output:
# > Europe
text = input()
num = int(input())

text = regexp_tokenize(text, "[A-z]+")

print(text[num])


# There is a text in the input. Split the text by sentences and print the result.
text = input()

print(sent_tokenize(text))


# There is a sentence in the input.
# Print the tokens using the method that returns word and punctuation tokens.
text = input()

print(word_tokenize(text))
