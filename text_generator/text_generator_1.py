from nltk import WhitespaceTokenizer

# In this project, we will use a corpus that contains the entire script of
# Game of Thrones. As the corpus will be used to "train" a probabilistic model
# that will predict the next word in a chain of words, the generated text
# will resemble the style and vocabulary of the source material.
# The naturalness of the generated text depends on the data.
# The bigger the corpus, the better the results. The corpus that we will be using
# in this project consists of around 300,000 tokens. That is not perfect,
# but it's good enough to get interesting results.
# In order to prepare the corpus for use in this project, we need to take
# the following important steps:
# Open and read the corpus from the provided file corpus.txt.
# The filename should be specified as user input. Note that the file is written
# in UTF-8 encoding, and the file should be in the same folder as your Python script.
# Break the corpus into individual words. To create a Markov model,
# we use the simplest form of tokenization: tokens are separated by
# whitespace characters such as spaces, tabulation, and newline characters.
# Punctuation marks should be left untouched since later on, they will play
# an important role in signaling where a sentence should end.
# Acquire and print the following information about the corpus under
# the section of the output called Corpus statistics:
# — the number of all tokens;
# — the number of all unique tokens, that is, the number of tokens without repetition.
# Each of the above should be in a new line.
# Take an integer as user input and print the token with the corresponding index.
# Repeat this process until the string exit is input. Also, make sure that
# the input index is actually an integer that falls in the range of the corpus.
# If that is not the case, print an error message and request a new input.
# Error messages should contain the types of errors (Type Error, Index Error, etc.).
# Each token should be printed in a new line.
file_name = input()

text = open(file_name, "r", encoding="utf-8")
full_text = text.read()

tbw = WhitespaceTokenizer()
tokenized_text = tbw.tokenize(full_text)

print("Corpus statistics")
print("All tokens:", len(tokenized_text))
print("Unique tokens:", len(set(tokenized_text)))

while True:
    index = input()
    if index != "exit":
        try:
            index = int(index)
            print(tokenized_text[index])
            continue
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
        except:
            print("Type Error. Please input an integer.")
            continue
    else:
        break

text.close()
