"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
import math


def binary_search(input_array, value):
    """Your code goes here."""
    temp_arr = input_array
    position = -1
    loops = int(math.floor(math.log(8) / math.log(2)))
    i = 0
    arr_len = len(temp_arr)
    start_pos = 0
    end_pos = arr_len
    while i != loops:
        position = (
            int(
                (end_pos - start_pos) / 2 - 1
                if (end_pos - start_pos) % 2 == 0
                else math.floor((end_pos - start_pos) / 2)
            )
            + start_pos
        )
        if (end_pos - start_pos) > 1:
            if temp_arr[position] == value:
                return position
            elif temp_arr[position] > value:
                # look left
                end_pos = position
            else:
                # look right
                start_pos = position + 1
                end_pos = arr_len
        elif (end_pos - start_pos) == 1:
            return position if temp_arr[position] == value else -1
        i += 1
    return position


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list, 11))
