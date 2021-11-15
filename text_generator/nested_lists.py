# Write a program that takes three strings as input and then constructs
# and prints a nested list from them – with first string as a first element,
# a list containing only second string as a second element and a list
# containing another list containing a third string as a third element.
str_1 = input()
str_2 = input()
str_3 = input()

print([str_1, [str_2], [[str_3]]])


# Several warm-up matches have been played at the tennis tournament.
# You have data on the victories and losses of some players.
# Save the names of the winners to a list and calculate the total number of victories.
# The input format:
# On the first line, you'll receive the integer n specifying a number of lines.
# The next n lines will look like either Name win or Name loss.
# The output format:
# On the first line, print out the list of all players that have won a match,
# repeat the names if necessary.
# Then output the total number of victories based on your list.
# Sample Input 1:
# > 2
# > Borg win
# > McEnroe loss
# Sample Output 1:
# > ['Borg']
# > 1
# Sample Input 2:
# > 3
# > McEnroe win
# > Borg loss
# > McEnroe win
# Sample Output 2:
# > ['McEnroe', 'McEnroe']
# > 2
wins = []
lines_number = int(input())

counter = 0
while counter < lines_number:
    name = input().split()
    if name[1] == "win":
        wins.append(name[0])
    counter += 1

print(wins)
print(len(wins))
