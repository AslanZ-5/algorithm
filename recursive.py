# PROBLEM 1:
# Given a string, find the first uppercase character.
# Solve using both an iterative and recursive solution

input_str_1 = 'lucidProgramming'
input_str_2 = 'LucidProgramming'
input_str_3 = 'lucidprogramming'


# iterative version of solution
def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return 'No uppercase character found'


# print(find_uppercase_iterative(input_str_1))
# print(find_uppercase_iterative(input_str_2))
# print(find_uppercase_iterative(input_str_3))


def find_uppercase_recursive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return 'No uppercase character found '
    return find_uppercase_recursive(input_str, idx + 1)


# print(find_uppercase_recursive(input_str_1))
# print(find_uppercase_recursive(input_str_2))
# print(find_uppercase_recursive(input_str_3))


# PROBLEM 2:
# Given a string, calculate the length of the string.
input_str = 'LucidProgramming'


def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return recursive_str_len(input_str[1:]) + 1


print(recursive_str_len(input_str))


# FACTORIAL
def rec_factorial(x):
    if x == 1:
        return 1
    return rec_factorial(x - 1) * x


# print(rec_factorial(5))


# FIBONACHI
def fibonachi(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)


# print(fibonachi(10))


# IS PALINDROM
def palindrom(st):
    if len(st) <= 1:
        return True
    if st[0] != st[-1]:
        return False
    return palindrom(st[1:-1])

# print(palindrom('nallan'))
