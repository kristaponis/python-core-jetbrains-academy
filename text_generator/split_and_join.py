# Read a date from the input given in the following format: YYYY-MM-DD.
# Print the year, month and day on separate lines.
date = input().split("-")

print("\n".join(date))


# Advanced input() handling is used to read input directly into
# several variables, for example:
#   x, y = input().split()
# Use it to print the next message with the two input values: "x of y"
x, y = input().split()

print(f"{x} of {y}")
