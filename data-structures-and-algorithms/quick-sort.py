"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def swap(array, pos1, pos2):
    if array[pos1] != array[pos2]:
        array[pos1], array[pos2] = array[pos2], array[pos1]

# Recursive quick sort with stacks


def quicksort(array):
    # initial setup
    arr_len = len(array)
    if len(array) > 1:
        left, right, pivot = [], [], array[arr_len - 1]
        array.pop()
        for i in range(arr_len-1):
            if array[i] >= pivot:
                right.append(array[i])
            else:
                left.append(array[i])
        return quicksort(left) + [pivot] + quicksort(right)
    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))

# 21 4 1 3 9 20 25 6 21 14

# 21 4 1 3 9 20 25 6 14 21
# 21 4 1 3 9 20 25 14 6 21
# 6 4 1 3 9 20 25 14 21 21
# 6 4 1 3 9 20 14 25 21 21
# 6 4 1 3 9 14 20 25 21 21
