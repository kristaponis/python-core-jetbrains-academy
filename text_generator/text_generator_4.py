import random
import nltk
from nltk import WhitespaceTokenizer
from collections import Counter

# Description:
# The model can already be used to predict the next word in a chain
# by feeding it any head (of a bigram) from the corpus and retrieving
# the most probable tail from the corresponding entry. But how do we
# start the chain, what should be the first word?
# Of course, we could choose a word manually, but this is an error-prone solution
# because we might take a word that is not in the corpus. A better way to start
# is to choose a random word from the corpus and feed it to the model
# so that it predicts the next word. After the next word is acquired, it should
# be used to predict the following word, and so on, thus continuing the chain.
# Objectives:
# Choose a random word from the corpus that will serve as the first word of the chain.
# The second word should be predicted by looking up the first word of the chain
# in the model and choosing the most probable next word from the set
# of possible follow-ups. Right now, an entry contains all the possible tails
# that might follow the selected head along with their corresponding repetition counts.
# Using the repetition counts, you will be able to choose the most probable option.
# The second step should be repeated until the length of the chain is 10 words,
# but this time, the current last word of the chain should be used to look up
# another probable word to continue the sentence.
# Using the algorithm described above, generate chains consisting of 10 tokens,
# join the resulting tokens together, and print them as a pseudo-sentence.
# Keep in mind that a pseudo-sentence can consist of multiple actual sentences,
# so having punctuation marks inside pseudo-sentences is completely valid.
# Generate and print 10 sentences like that. Keep in mind that every
# generated pseudo-sentence should be on a new line.
# You should only print the output of the current stage and not the previous one.
# The name of the file that contains the corpus should be given as a command line input.
# file_name = input()

text = open("corpus.txt", "r", encoding="utf-8")
full_text = text.read()
tbw = WhitespaceTokenizer()
tokenized_text = tbw.tokenize(full_text)
random_word = random.choice(tokenized_text)
text_bigrams = list(nltk.bigrams(tokenized_text))
bigrams_dict = {}

for bigram in text_bigrams:
    bigrams_dict.setdefault(bigram[0], []).append(bigram[1])

for i in range(10):
    line = []
    for j in range(10):
        freq_item = Counter(bigrams_dict[random_word])
        print()
        possible_tail = random.choices(list(freq_item.keys()), weights=list(freq_item.values()))
        line.append(possible_tail[0])
    print(" ".join(line))

text.close()
