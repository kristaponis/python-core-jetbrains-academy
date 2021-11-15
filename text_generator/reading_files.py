# You are given the file test.txt.
# Read it and print the first letter from each line.
test = open("test.txt")

for line in test:
    print(line[0])

test.close()


# Read the file sample.txt and print the number of lines that this file has.
lines = open("sample.txt")
counter = 0

for line in lines:
    counter += 1

print(counter)

lines.close()
