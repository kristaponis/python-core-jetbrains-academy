import random

# Everybody wants to speak like master Yoda sometimes.
# Let's try to implement a program that will help us with it.
# First, we turn the string of words into a list using the string.split() method.
# Then use the function random.seed(43) and rearrange the obtained sequence.
# To turn the list back into a string, use ' '.join(list).
# Print the message in the end. Note: you have to use random.seed(43) in this task!
words = input().split(" ")

seed = 43
random.seed(seed)
random.shuffle(words)

print(' '.join(words))
