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


# print(recursive_str_len(input_str))


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

# Given a string, count the number of consonats.
# Note a consonant is a letter that is not a vowel,
# i.e. a letter that is not a,e,o,i or u

input_str4 = 'abc de'
input_str5 = 'LuCiDProGrAmMiNG'
vowel = 'aeiuo'


def iterative_count_consonants(s):
    c = 0
    for i in s.lower():
        if i not in vowel and i.isalpha():
            c += 1
    return c


def recursive_count_consonants(s):
    if s == '':
        return 0
    if s[0].lower() not in vowel and s[0].isalpha():
        return 1 + recursive_count_consonants(s[1:])
    else:
        return recursive_count_consonants(s[1:])


# print(iterative_count_consonants(input_str5))
# print(recursive_count_consonants(input_str5))


# Given two numbers, find their product using recursion.
x = 5
y = 3


def recursive_product(x, y):
    if y == 0:
        return 0
    return recursive_product(x, y - 1) + x


print(recursive_product(x, y))
