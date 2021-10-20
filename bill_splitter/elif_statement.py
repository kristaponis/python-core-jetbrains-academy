# One way to classify the languages of the world is by looking
# at their morphological systems. One classification is based
# on the index of synthesis that reflects
# the average number of morphemes in a word.
# The values vary between 1 and 4 and there are 3 types of languages
# according to that system. Here they are:
# Analytic      — less than 2
# Synthetic     — from 2 to 3 (inclusively)
# Polysynthetic — more than 3
# Write a program that given the index of synthesis determines
# the type of the language.
# The input format:
# The value of the index of synthesis.
# The output format:
# The type of language.
index = float(input())

if index < 2:
    print("Analytic")
elif 2 <= index <= 3:
    print("Synthetic")
elif index > 3:
    print("Polysynthetic")


# In a computer game, each gamer has an army of units.
# Write a program that will classify the army of your enemies
# corresponding to the following rules:
# less than 1: no army
# from 1 to 9: few
# from 10 to 49: pack
# from 50 to 499: horde
# from 500 to 999: swarm
# 1000 and more: legion
# The program should read the number of units and output
# the corresponding category.
units = int(input())

few = units < 10
pack = units < 50
horde = units < 500
swarm = units < 1000

if units > 0:
    if few:
        print("few")
    elif pack:
        print("pack")
    elif horde:
        print("horde")
    elif swarm:
        print("swarm")
    else:
        print("legion")
else:
    print("no army")


# Let's write a simple calculator! It will read 3 lines:
#   the first number
#   the second number
#   the arithmetic operation.
# Numbers are floats! The output is the result of the following:
# first_number operation second_number.
# Operations are: +, -, /, *, mod, pow, div.
# mod — modulo operation, i.e. the remainder of the division first_number % second_number,
# pow — exponentiation, the first number will be the base
# and the second — the power: first_number ** second_number,
# div — integer division first_number // second_number.
# Note that if the second number is 0 and you want to perform any of the operations /,
# mod, or div, the calculator should say "Division by 0!"
first_number = float(input())
second_number = float(input())
operation = input()

if operation in "/, div, mod":
    if second_number == 0:
        print("Division by 0!")
    elif operation == "/":
        print(first_number / second_number)
    elif operation == "mod":
        print(first_number % second_number)
    else:
        print(first_number // second_number)
elif operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
else:
    print(first_number ** second_number)


# In a farming game, you can buy certain animals for a specific price.
# As a player, you want to buy the most useful (i.e. the most expensive) animal.
# Here are the animals and their prices:
# Chicken: 23
# Goat: 678
# Pig: 1296
# Cow: 3848
# Sheep: 6769
# Write a program that determines what is the most expensive animal that
# the user can buy with their money and how many of them they can buy.
# Note that you should only find one kind of animal to buy (the most expensive).
# You don't need to mention any alternative options.
# For example, if the user has 710 coins, your program should output 1 goat,
# but not 1 goat\n30 chickens or anything like that. 
# The input format:
# The money that the user has.
# The output format:
# How many animals the user can afford, for example, 20 chickens.
# If the user cannot afford any animal, write None.
money = int(input())

animals = {"Chicken": 23, "Goat": 678, "Pig": 1296, "Cow": 3848, "Sheep": 6769}

if money >= animals['Sheep']:
    num = money // animals['Sheep']
    print(num, "sheep")
elif money >= animals['Cow'] < animals['Sheep']:
    num = money // animals['Cow']
    if num == 1:
        print(num, "cow")
    else:
        print(num, "cows")
elif money >= animals['Pig'] < animals['Cow']:
    num = money // animals['Pig']
    if num == 1:
        print(num, "pig")
    else:
        print(num, "pigs")
elif money >= animals['Goat'] < animals['Pig']:
    num = money // animals['Goat']
    if num == 1:
        print(num, "goat")
    else:
        print(num, "goats")
elif money >= animals['Chicken'] < animals['Goat']:
    num = money // animals['Chicken']
    if num == 1:
        print(num, "chicken")
    else:
        print(num, "chickens")
else:
    print(None)


# The world of elementary particles is rather complex. There are many
# different classes and they can interact in a rather interesting way.
# Two important characteristics of the elementary particles are the spin
# and the electric charge. Here are some of the elementary particles:
# Particle	Class	Spin	Electric charge
# Strange   Quark	1/2	    -1/3
# Charm	    Quark	1/2	    2/3
# Electron	Lepton	1/2	    -1
# Neutrino	Lepton	1/2	    0
# Photon	Boson	1	    0
# Write a program that returns the particle and
# its class based on its spin and electric charge.
# The input format:
# Two lines: first the spin of the particle, then its charge.
# You do NOT have to convert these values to floats.
# The output format:
# The particle and its class separated by a space.
spin = input()
e_charge = input()

if spin == "1":
    print("Photon Boson")
elif spin == "1/2" and e_charge == "0":
    print("Neutrino Lepton")
elif e_charge == "-1":
    print("Electron Lepton")
elif e_charge == "2/3":
    print("Charm Quark")
else:
    print("Strange Quark")
