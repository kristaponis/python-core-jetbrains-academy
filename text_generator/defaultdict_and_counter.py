from collections import Counter

# Suppose we have a short sentence and an empty dictionary.
# Calculate the frequencies for each word in this sentence.
sentence = 'Chess set is a chessboard and a set of chessmen.'
frequencies = {}

sentence_list = sentence.lower().split()

for word in sentence_list:
    frequencies.setdefault(word, 0)
    frequencies[word] += 1

print(frequencies["chess"])


# The Counter class provides some special methods that we
# didn't cover in the topic. Here, you will need to use the elements() function.
# Take a string from a user as input, turn it into lowercase and split it,
# create a Counter dictionary from it, and then print the sorted
# list of elements that the dictionary consists of.
# Sample Input:
# Chessboard is a square board divided into sixty-four.
# Sample Output:
# ['a', 'board', 'chessboard', 'divided', 'into', 'is', 'sixty-four', 'square']
text = input().lower().split()

c = Counter(text)

print(sorted(c.elements()))


# Emilia is working in a bank and she has data about some transactions.
# The transactions are given as a list of tuples named transactions
# where the first element of the tuple is the account id
# and the second — the sum spent in the transaction. Help Emilia turn
# this data into a dictionary where a key is an account id and its value is
# the list of the money spent in transactions. The sums of money on this list
# should be in their original order! The new dictionary should
# be named transaction_dict. For example, transaction_dict may look
# like this {546: [987.65]}. The value of the key 546 should be [987.65]
# because the account with the id 546 made only one transaction.
transactions = [(38177, 34.38), (876, 999.99), (654276, 653678),
                (54366, 0.99), (546, 987.65), (876, 3456), (654276, 0.55),
                (38177, 876.75), (876, 98.7)]

transaction_dict = {}

for transaction in transactions:
    transaction_dict.setdefault(transaction[0], []).append(transaction[1])

print(transaction_dict)


# Below you can see a string with a text. Read the number n from the input
# and print out the n most frequent words from the text with their frequencies.
# If several words have the same frequency, they should go in the order
# they appear in the text. The word and the frequency should be separated
# by whitespace and each word should be on a new line.
text = '''all I want is a proper cup of coffee made in a proper copper coffee pot.
        I may be off my dot but I want a cup of coffee from a proper coffee pot.'''

freq_counter = Counter(text.split())

num = int(input())
new_freq = freq_counter.most_common(num)

counter = 0
while counter < num:
    print(new_freq[counter][0], new_freq[counter][1])
    counter += 1
