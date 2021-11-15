from random import choice, choices
from collections import defaultdict, Counter

# Complete rewrite.
# Description:
# The generated text finally looks like actual sentences! It's a great step
# in the right direction, but do they actually make sense? Unfortunately,
# the algorithm most likely generates gibberish that can hardly be called
# a product of an artificial "intelligence". This happens because the algorithm
# considers nothing but the preceding word when trying to predict the next one
# in the chain. It basically works like a person who forgets the beginning
# of their sentence while speaking and pronounces the first probable word
# that comes into their mind without really connecting it to the original idea
# of the sentence.
# Objectives:
# Right now, the model is based on bigrams, that is, we only consider one word
# when trying to predict the next word in the chain. The algorithm should be
# extended so that it can use not only bigrams but also trigrams.
# We have already talked about trigrams in Stage 2. They are very similar
# to bigrams, the only difference being their length: trigrams consist of three
# tokens instead of just two. In the case of trigrams, every head should consist
# of two tokens. Tails should stay the same length as before since we are still
# aiming to predict the next word in the chain.
# This change implies the following tasks:
# The list of bigrams should be transformed into a list of trigrams.
# It should still consist of heads and tails, but now, heads should consist
# of two space-separated tokens concatenated into a single string.
# The tails should still consist of one token.
# For example: head — winter is, tail — coming.
# The model should be trained based on the list of trigrams. The model creation
# requires no modifications since trigrams still consist of a head and a tail.
# The beginning of the chain should be a randomly chosen head from the model,
# not just any word from the corpus. When predicting the next word, the model
# should be fed the concatenation of the last two tokens of the chain
# separated by a space. After making all these modifications,
# the output should look rather similar to the result of the previous stage,
# but now the generated pseudo-sentences should make a little more sense.
class TextGenerator:
    def __init__(self):
        self.path = input()
        self.tokens = self.tokenise_text()
        self.trigrams = self.trigrams()

    def read_file(self):
        with open(self.path) as file:
            text = file.read()
        return text

    def tokenise_text(self):
        text = self.read_file()
        return text.split()

    def trigrams(self):
        trigrams = defaultdict(Counter)
        for i in range(len(self.tokens) - 2):
            trigrams[" ".join(self.tokens[i:i + 2])].update((self.tokens[i + 2],))
        return trigrams

    def first(self):
        words = [pair for pair in list(self.trigrams) if pair.split()[0][0].isupper() and pair.split()[0][-1] not in "!?."]
        return choice(words).split()

    def sentence(self, n=5):
        line = []
        while True:
            if len(line) == 0:
                line = self.first()
            word1 = " ".join(line[-2:])
            word2 = choices(list(self.trigrams[word1].keys()), list(self.trigrams[word1].values()))
            line.append(*word2)

            if word2[0][-1] in ".!?":
                if len(line) < n:
                    line = []
                    continue
                return " ".join(line)


textgen = TextGenerator()

for _ in range(10):
    print(textgen.sentence())
