"""
Quadratic running time - O(n2)
    The runtime is a quadratic function of the size of the input.
    A naive implementation of finding duplicate values in a list, in which
    each item has to be checked twice, is an example of a quadratic algorithm.

Selection sort is a sorting algorithm that selects the
 smallest element from an unsorted list in
 each iteration and places that element at the
  beginning of the unsorted list.

"""


def selection_sorting(arr):
    for i in range(0, len(arr) - 1):
        cur_min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]  # swap


arr = [2, 6, 5, 1, 3, 4]
