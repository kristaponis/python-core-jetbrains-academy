import math

# Write a program that calculates the area of a triangle by its three sides.
# Write the program following Heron's formula:
#       ________________
# S = ⎷ p(p−a)(p−b)(p−c)
# 
# where p = 2 / (a+b+c) is a half-perimeter of the triangle.
# On the input, the program has integers, and the output should be
# a real number corresponding to the area of the triangle.
a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2

s = p * (p - a) * (p - b) * (p - c)

print(math.sqrt(s))


# Write a program that reads an integer that represents the radius
# of a given circle and calculates its area. To calculate the area of a circle,
# use the following formula: 
# 
# S = πr^^2
# 
# Print the result rounded to 2 decimal places.
r = int(input())

s = math.pi * r ** 2

print(round(s, 2))


# Write a program that prints the fourth root from a given real number.
# The square root function is located in the math module. Try to find and apply it.
# Do not round the result.
import math

user_input = float(input())

print(math.sqrt(math.sqrt(user_input)))


# Write a program that reads two integers (the first is always positive) and
# calculates the logarithmic value of the first integer with
# the second integer as a base. If the second integer is negative, 0 or 1,
# return the natural log of the first number.
# Use the function log() from the math module.
# With one argument, it returns the natural logarithm of a number.
# It can also take two arguments: a number and a logarithmic base.
# Print the result rounded to 2 decimal places.
x = int(input())
y = int(input())

if y > 1:
    print(round(math.log(x, y), 2))
else:
    print(round(math.log(x), 2))
