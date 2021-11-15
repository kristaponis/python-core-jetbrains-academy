import re

# Fill the value of the regex variable with a regular expression.
# It should match the "python" substring (without quotes) when it
# is located at the very beginning of some alphanumeric sequence.
# In other words, it should be a part of a bigger word.
# For example, your regular expression should match the strings
# "python3", "pythonist", "pythonnn" (without quotes), but not the strings
# "python", "what is python?", "python is worse than java" (without quotes).
regex = r"python\w"


# Write a regular expression that matches a conclusive statement
# "I love Python" (without quotes). "Conclusive" means that these words
# should be the last in the text, and nothing else should follow them.
regex = "I love Python$"


# An alien from some distant planet got lost in our world.
# He asks you to find his compatriots and contact them.
# To search the Internet for them, fill the value of the regex variable
# with a regular expression that matches common names of the inhabitants
# of that planet. The names are developed according to the following rules:
#     the first symbol is an alphanumeric character
#     the second symbol is a digit
#     there may be another digit following the first one
#     the last symbol is not a whitespace or alphanumeric character
regex = r"\w\d*[^\w\s]$"
