# Eugene and Rose decided to travel abroad. For convenience, they will go
# to a country where one of them has already been, but not where they both have.
# Output a set of potential countries for them.
eugene = set(input().split())
rose = set(input().split())

print(eugene ^ rose)


# Some states of the USA share their names with rivers.
# We have defined two variables with respective place names.
# Print out a new set with river names that don't overlap with given states.
rivers = set(input().split())
states = set(input().split())

print(rivers - states)


# Imagine you have two lists of names: people from the first list play the violin,
# while people from the second one happen to speak German.
# Print a set with names of those who can do both.
violinists = set(input().split(', '))
german_speakers = set(input().split(', '))

print(violinists.intersection(german_speakers))


# You are given several sets with names of students in different classes.
# Output the set containing names of all the students.
gryffindor = set(input().split())
ravenclaw = set(input().split())
slytherin = set(input().split())
hufflepuff = set(input().split())

print(gryffindor | ravenclaw | slytherin | hufflepuff)


# Using the three given sets, write a code that creates a set
# containing the elements that all of the original sets have in common.
# Output this resulting set.
set_1 = set(input().split())
set_2 = set(input().split())
set_3 = set(input().split())

planets = [set_1, set_2, set_3]
common_planet = set.intersection(*planets)

print(common_planet)
