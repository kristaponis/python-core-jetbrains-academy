# How would you write a regexp pattern that matches a person whose
# last name is Smith? Note that your pattern must match such names as:
#     Will Smith
#     Bessie Smith
#     Anna Nicole Smith
# And should not match:
#     will Smith (lowercase first name)
#     Bessie smith (lowercase last name)
#     Anna NicoleSmith (no space between the names)
#     Smith (no first name)
template = r"[A-Z][\w+\s]+ [A-Z]mith$"


# Imagine you have to write a child poem about animals.
# But you struggle with finding appropriate rhymes for the word bunny.
# Write a regexp pattern that will match appropriate words: they should be
# from 4 to 7 letters long and end with -nny or -ney.
# Note that the pattern should only match strings containing
# letters, i.e. such string as 123nny should not be considered a proper result.
template = "[a-z]{1,4}n[ne]y$"
