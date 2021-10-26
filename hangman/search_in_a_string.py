# Read the input, find the starting index of the substring "old",
# then search backward from the end of the string for the same substring,
# and print the bigger value of the two.
# Sample Input:
# old macdonald had an old farm
sentence = input()

first_old = sentence.find("old")
last_old = sentence.rfind("old")

print(first_old if first_old > last_old else last_old)


# Write a program that takes two strings, checks whether the first string
# contains the second one and prints the result of the membership test.
a = input()
b = input()

print(b in a)


# Read the input and count how many times the substring "happy" appears in it.
# Print the number.
# Sample Input:
# If you're happy and you know it, clap your hands
# If you're happy and you know it, clap your hands
# If you're happy and you know it, then your face will surely show it
# If you're happy and you know it, clap your hands
# If you're happy and you know it, stomp your feet
# If you're happy and you know it, stomp your feet
# If you're happy and you know it, then your face will surely show it
# If you're happy and you know it, stomp your feet
# If you're happy and you know it, shout 'Hurray!' (Hurray!)
# If you're happy and you know it, shout 'Hurray!' (Hurray!)
# If you're happy and you know it, then your face will surely show it
# If you're happy and you know it, shout 'Hurray!' (Hurray!)
# If you're happy and you know it, do all three (hurray!)
# If you're happy and you know it, do all three (hurray!)
# If you're happy and you know it, then your face will surely show it
# If you're happy and you know it, do all three (hurray!)
sentence = input()

print(sentence.count("happy"))
