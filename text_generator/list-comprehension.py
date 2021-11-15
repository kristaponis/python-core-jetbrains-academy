# list comprehension syntax
# new_list = [x for x in some_iterable]
#
# the equivalent code with for in
# new_list = []
# for x in some_iterable:
#     new_list.append(x)
#
# list comprehension with condition
# new_list = [x for x in some_iterable if condition]

# Print a list of numbers from 1 to 1000 that can be divided by 3.
# min_value = 1
# max_value = 1001

# new_list = [x for x in range(min_value, max_value) if x % 3 == 0]

# print(new_list)


# The list seconds is a list of numbers that represent seconds.
# Convert the number of seconds to full days and print the list
# that contains these values. The number of full days should be an int value.
seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]

days = [x // 60 // 60 // 24 for x in seconds]

print(days)


# Write a program that takes a list with words, creates a new list of words
# that start with the letter "a" in the first list, and prints it. Some words may
# begin with the capital A! Leave them in their original form in the resulting list.
words = ['apple', 'pear', 'banana', 'Ananas']

new_list = [x for x in words if x.lower().startswith("a")]

print(new_list)


# Write a program that divides numbers into two lists depending on whether
# they are greater than or less than 5. You don't have to include number 5 itself.
numbers = [int(n) for n in input()]

less_than_5 = [x for x in numbers if x < 5]
greater_than_5 = [x for x in numbers if x > 5]

print(less_than_5)
print(greater_than_5)


# Given a list of words in the code below,
# create a list of lengths of those words and print it.
words = ["apple", "it", "creek", "pelican", "subsequent", "horse","apothecary"]

word_lengths = [len(x) for x in words]

print(word_lengths)
