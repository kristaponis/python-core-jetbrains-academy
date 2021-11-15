import nltk
from nltk import WhitespaceTokenizer

# Description:
# After the training data is acquired and preprocessed, it has to be transformed
# into a Markov chain model. The first step is to map the connections
# between tokens in the corpus. For this, we are going to use bigrams.
# Objectives:
# Transform the corpus into a collection of bigrams. The results should contain
# all the possible bigrams from the corpus, which means that:
# — Every token from the corpus should be a head of a bigram with the exception
# of the last token which cannot become a head since nothing follows it;
# — Every token from the corpus should be a tail of a bigram with the exception
# of the first token which cannot possibly be the tail of a bigram
# because nothing precedes it.
# Output the number of all bigrams in the corpus.
# Take an integer as user input and print the bigrams with the corresponding index.
# Repeat this process until the string exit is input. Also, make sure that
# the input is actually an integer that falls in the range of the collection of bigrams.
# If that is not the case, print an error message and request a new input.
# Error messages should contain the types
# of errors (Type Error, Value Error, Index Error, etc.). Each bigram should have
# the format Head: [head] Tail: [tail] and should be printed in a new line.
# You should only print the output of the current stage and not the previous one,
# but like in the previous stage, the name of the file that contains the corpus
# should be given as user input.
file_name = input()

text = open(file_name, "r", encoding="utf-8")
full_text = text.read()

tbw = WhitespaceTokenizer()
tokenized_text = tbw.tokenize(full_text)

text_bigrams = list(nltk.bigrams(tokenized_text))

print(len(text_bigrams))

while True:
    index = input()
    if index != "exit":
        try:
            index = int(index)
            print(f"Head: {text_bigrams[index][0]}\tTail: {text_bigrams[index][1]}")
            continue
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
        except:
            print("Type Error. Please input an integer.")
            continue
    else:
        break

text.close()

