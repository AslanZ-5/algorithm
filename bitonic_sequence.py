"""
Define a bitonic sequence as a sequence of integers such that:
 x_1 <= ... <= x_k >= ... >= x_n-1 for some k, 0 <= k<n.

 for example:
 1,2,3,4,5,4,3,2,1

 is a bitonic sequence. Write a program to find the largest element in such
 a sequence. In the example above, the program should return "5".
 We assume that such a "peak" element exists.
"""

# peak element is "5"
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# peak element is "4"
A2 = [1, 2, 3, 4, 1]

# Peak element is "6"
A3 = [1,2,3,4,5,6,1]


def find_hidhest_number(A):
    low = 0
    high = len(A) - 1
    if len(A) < 3:
        return None
    while low < high:
        mid = (low + high) // 2
        mid_left = A[mid - 1] if mid -1 > 0 else float("-inf")
        mid_right = A[mid + 1] if mid + 1 < len(A) else float("inf")
        if A[mid] > mid_left and A[mid] > mid_right:
            return A[mid]
        elif mid_right > mid_left:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(find_hidhest_number(A3))
