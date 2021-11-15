# Anthony keeps track of what he eats: he writes down how many calories are in his meals.
# Use the list of dictionaries to calculate the total amount of calories per day and print it.
# The sample input will look like:
# meals = [
#         {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
#         {"title": "Italian salad with fusilli and ham", "kcal": 320},
#         {"title": "Bulgur with vegetables", "kcal": 350},
#         {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
#         {"title": "Oatmeal with honey and peanuts", "kcal": 440}]
# The output in this case should be 1705.
meals = [
        {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
        {"title": "Italian salad with fusilli and ham", "kcal": 320},
        {"title": "Bulgur with vegetables", "kcal": 350},
        {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
        {"title": "Oatmeal with honey and peanuts", "kcal": 440}]

total = 0

for meal in meals:
    total += meal["kcal"]

print(total)


# In a standard deck of cards, there are 13 of each suit.
# There are numbered cards (from 2 to 10) and face cards (Jack, Queen, King, and Ace).
# If we were to rank the face cards, Jack would be 11, Queen 12, King 13, and the Ace — 14.
# Write a program that calculates the average rank of one hand of cards.
# Don't forget to consider the rank of the face cards.
# The input format:
# Six values of cards, each on a separate line.
# The output format:
# The average rank of the hand.
faces = {"Ace": 14, "King": 13, "Queen": 12, "Jack": 11}
cards = []
total = 0

for _ in range(6):
    user_card = input()
    cards.append(user_card)

for card in cards:
    if faces.get(card) is None:
        total += int(card)
    else:
        total += faces.get(card)

print(total / 6)


# Write a program that creates a dictionary, in which keys are latin letters,
# and values are their doubling:
# {a: aa, b: bb, ..., z: zz}
from string import ascii_lowercase

double_alphabet = {}

for letter in ascii_lowercase:
    double_alphabet[letter] = letter * 2
