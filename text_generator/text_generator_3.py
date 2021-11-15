import nltk
from nltk import WhitespaceTokenizer
from collections import Counter

# Description:
# This is the final step where we will work on creating a Markov chain model.
# We will use the data prepared in the first two stages and transform it into a model.
# This model will contain probabilistic information that will tell us
# what the next word in a chain might be. We already have a list of all bigrams
# from the corpus. As we discussed earlier, this can already be used to make
# some naive predictions. There is a problem, though: right now our data
# contains a lot of repetition. As we have seen at the first stage,
# the total number of tokens is almost 10 times greater than
# the number of unique tokens. This ratio must be about the same
# in the list of bigrams. Some bigrams might be very common, others — relatively rare.
# At the moment, we have no way of telling which are which.
# To resolve this problem, we will make a simplified version of a Markov chain model.
# Objectives:
# The data should be reorganized in such a way that every head is repeated only once,
# and all the possible tails can be directly accessed by querying that head.
# For example: head — good, tails — night, bye, bye, night, to, to, bye, boy.
# As you can see, there are still some repetitions among the tails.
# Instead of repeating tails every time they occur, each tail should appear
# only once and the number of repetitions should be stored as an integer.
# For example, the previous example should look like this:
# head — good, tails — night: 2, bye: 3, to: 2, boy: 1.
# You can see that the data is more readable after this transformation!
# Besides creating the model, we should also check that it works correctly.
# To test it, let's take a string as user input and print all the possible tails
# and their corresponding counts. If the model does not contain the specified head
# print the following error message Key Error.
# The requested word is not in the model. Please input another word.
# and ask for another until it is valid. Repeat until the string exit is input.
file_name = input()

text = open(file_name, "r", encoding="utf-8")
full_text = text.read()
tbw = WhitespaceTokenizer()
tokenized_text = tbw.tokenize(full_text)
text_bigrams = list(nltk.bigrams(tokenized_text))
bigrams_dict = {}

for bigram in text_bigrams:
    bigrams_dict.setdefault(bigram[0], []).append(bigram[1])

while True:
    word = input()
    if word != "exit":
        try:
            print(f"Head: {word}")
            freq_item = Counter(bigrams_dict[word])
            for key, value in freq_item.items():
                print(f"Tail: {key}\tCount: {value}")
            print()
            continue
        except KeyError:
            print('Key Error. The requested word is not in the model. Please input another word.')
            continue
    else:
        break

text.close()


