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
    while b <= k:

        b = a**2
        a +=1
    return b

print(integer_square_root(300))