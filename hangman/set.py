# You are assisting in a psychological experiment. To test short-term memory,
# a researcher gives a set of numbers to each volunteer and asks to repeat
# all of them. The order does not matter and repeats are allowed.
# The input has been read into two variables for you.
# If the volunteer remembers all numbers correctly, print True, otherwise,
# you should output False.
# Sample Input:
# 1 2 3 4 5
# 5 4 1 2 1 3
# Sample Output:
# True
numbers = input().split()
answers = input().split()

numbers = set(numbers)
answers = set(answers)

if numbers == answers:
    print(True)
else:
    print(False)
