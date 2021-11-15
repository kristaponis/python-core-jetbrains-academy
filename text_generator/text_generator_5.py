import re
import random
import nltk
from collections import Counter

# Description:
# The algorithm is now capable of generating pseudo-random text based on Markov
# chains. The problem is that the resulting text does not resemble sentences at all.
# First, the resulting text is always ten tokens long.
# Second, it does not always start with capital letters.
# Third, it usually does not even end with correct punctuation such as periods,
# exclamation marks, or question marks.
# Objectives:
# Make the algorithm more realistic by generating pseudo-sentences
# instead of just random text. The sentences that are being generated should:
# — always start with capitalized words ("This is beautiful.", etc.);
# — not start with a word that ends with a sentence-ending punctuation mark
# ("Okay.", "Nice.", "Good.", "Look!", "Jon!", etc.);
# — always end with a sentence-ending punctuation mark like ., !, or ?;
# — should not be shorter than 5 tokens.
# Generate and print exactly 10 pseudo-sentences that meet these criteria.
# A pseudo-sentence should end when the first sentence-ending punctuation mark
# is encountered after the minimal sentence length (5 tokens) is reached.
# file_name = input()

text = open("corpus.txt", "r", encoding="utf-8")
full_text = text.read()
tokenized_text = full_text.split()
text_bigrams = list(nltk.bigrams(tokenized_text))
bigrams_dict = {}

for bigram in text_bigrams:
    bigrams_dict.setdefault(bigram[0], []).append(bigram[1])

for i in range(10):
    line = []
    while True:
        random_word = random.choice(tokenized_text)
        freq_item = Counter(bigrams_dict[random_word])
        possible_tail = random.choices(list(freq_item.keys()), weights=list(freq_item.values()))
        line.append(possible_tail[0])
        if not re.match(r"^[A-Z]", line[0]):
            line = []
            continue
        if re.match(r"^[A-Z]\w*[.?!]", line[0]):
            line = []
            continue
        if len(line) >= 5 and len(line) <= 10:
            if re.match(r".+[.?!]$", line[-1]):
                break
            else:
                line = line[:5]
                continue
    print(" ".join(line))

text.close()
