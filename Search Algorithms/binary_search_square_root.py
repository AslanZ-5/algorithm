"""
Write a function that takes a non-negative integer and returns
the largest integer whose square is less or equal to
the integer given.
Example:
    Assume input is integer 300.
    Then the expected output of the function should be 17,
    since 17^2 = 289 < 300. Note that 18^2 = 324 > 300,
    so the number 17 is the correct response.

"""


def integer_square_root(k):
    a = 1
    b = 0
    while b < k:
        if (a + 1) ** 2 > k:
            return a
        b = a ** 2
        a += 1
    return 0


def integer_square_root_binary(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if mid ** 2 <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


# print(integer_square_root(300))
print(integer_square_root_binary(300))
print((17+20)//2)