# Write a program that reads numbers until a user enters 55.
# Once 55 is entered, stop reading the input,
# print out how many numbers have been entered, their total sum,
# and average (do the rounding this way: round(number)).
# Do NOT include 55 in your calculations and
# print each resulting value on a new line in the order given above.
count = 0
total = 0
fifty_five = 55

while True:
    user_input = int(input())
    if user_input == fifty_five:
        break
    else:
        count += 1
        total += user_input

print(count)
print(total)
print(round(total / count))

# Write a program that prints all positive even numbers less than the input number.
# Please, use the while loop for that.
# The input format:
# The maximum number N varying from 1 to 200.
# The output format:
# All positive even numbers that are less than N. Print them in the ascending order.
# Each number must be on a separate line.
number = int(input())
count = 1

while count < number:
    if count % 2 == 0:
        print(count)
    count += 1
