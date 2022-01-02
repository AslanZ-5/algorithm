"""
Big O notation is a method for determining how fast an algorithm is.
 Using Big O notation, we can learn whether
 our algorithm is fast or slow. This knowledge
  lets us design better algorithms.
  """


# O(1) Constant
def func_constant(values):
    """Prints first item in a list of values"""
    print(values[0])
    """It doesn't matter how large my values list becomes,
    the function/algo will only grab the indexed position 0 in that list"""


# O(n) linear

def func_lin(lst):
    """Takes in list and prints out all values"""
    for val in lst:
        print(val)
    """
    Every values will print for the list, each time, so the larger
    the list gets the larger BigO, this algorithm will scale linearly with n>
    """


# O(n^2) Quadratic
def func_quad(lst):
    """
    Prints pairs for every item in list.
    """
    for item in lst:
        for item_2 in lst:
            print(item, item_2)
    """
    - two loops, one nested inside another.
    - for a list of n items, we will have to perform n operations for every item in the list! This 
      means in total, we will perform n times n assignments, or n^2. So a list of 10 items will have 10^2, or 100 operations.
      You can see how dangerous this can get for very large inputs! this is why Big-O is so important to be aware of!
    - hence, the input of 3 gives us 9 outputs iterations.
    """


# Calculating Scale of Big-O
"""
insignificant terms drop out of Big-O notation
When it comes to Big O notation we only care about the most significant terms, remember as the input grows larger only the 
fastest growing terms will matter.
    - like taking towards infinity 
"""


def print_once(lst):
    """Prints all items once O(n)"""
    for val in lst:
        print(val)


def print_3(lst):
    """
    Prints all items three times
    This algorithm will run 3 times for each n, so this becomes an order of 3(n). It is still linear
    More importantly, 3(infinity) is not really different than (infinity) and we can drop insignificant
    constants.
    So this too is O(n).
    """

    for val in lst:
        print(val)

    for val in lst:
        print(val)

    for val in lst:
        print(val)


def comp(lst):
    """
    This is function prints the first item O(1) it is a constant
    Then is prints the first 1/2 of the list o(n/2)
    Then prints a string 10 times O(n) it is a constant
    """
    print (lst[0])

    midpoint = len(lst)//2

    for val in lst[:midpoint]:
        print(val)
    for x in range(10):
        print('number')

    """
     O(1+ n/2 + 10)
     An n gets larger and larger (scales up) you can easily see how the 1 and the 10 quickly begin to mean nothing.
     And the //2 will begin to have no effect either 
     End up with O(n)
    """


