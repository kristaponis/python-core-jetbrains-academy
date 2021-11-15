# Sometimes it might be useful to convert text from CamelCase to snake_case.
# The main trick is to find the correct place where to insert an underscore.
# Let's make a rule that an underscore should be inserted right before a capital letter
# but only if it's not the very first letter.
# In case it is, just convert it to lowercase, and do not insert an underscore before it,
# so CamelCase becomes camel_case.
# The input format:
# Read a word or a phrase written in lowerCamelCase
# The output format:
# Print out words in lowercase and separate them by underscores.
word = input()
word = word[0].lower() + word[1:]
final = ""
snake = "_"

for letter in word:
    if letter.islower():
        final += letter
    elif letter.isupper():
        final += snake + letter.lower()

print(final)
