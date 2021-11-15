# You play a game with your friends. You give them a non-empty list of integers
# and they create a list of lists, which contains your list
# and some other non-empty lists in some order.
# Your task is to find your list among other lists.
# You should write a function find_my_list(all_lists, my_list),
# where the first argument is the list of lists and the second argument
# is the list of integers that you should find.
# The function should return the position of my_list in all_lists.
# The lists in all_lists are numbered from zero.
# It's guaranteed that an element exists in all_lists.
def find_my_list(lists, my_list):
    for idx, lst in enumerate(lists):
        if lst is my_list:
            return idx
    return None


# Write a function check_values that accepts two values
# (for example, 0 and 1, or "string" and []) and checks if both of them are True.
# To achieve this, convert the values via the built-in bool() function.
# If both values are True, then your function should return True, otherwise False.
def check_values(first_value, second_value):
    return bool(first_value and second_value)

