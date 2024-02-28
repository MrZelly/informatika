import random

def quicksort(array, left, right):
    if left < right:
        pivot_index = partition(array, left, right)
        quicksort(array, left, pivot_index - 1)
        quicksort(array, pivot_index + 1, right)

def partition(array, left, right):
    pivot_value = array[right]

    low = left - 1

    for i in range(left, right):
        if array[i] < pivot_value:
            low += 1
            array[i], array[low] = array[low], array[i]

    array[low + 1], array[right] = array[right], array[low + 1]

    return low + 1

array = []

for i in range(5000):
    array.append(i)
random.shuffle(array)

quicksort(array, 0, len(array) - 1)
