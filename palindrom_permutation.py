"""
Given a string, write a function to check if it is
a permutation of a palindrome. A palindrome is a word
or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The
palindrome does not need to be limited to just dictionary
words
"""

palim_perm = 'Tact Coa'
not_palin_perm = "This is not a palindrome permutation"


def is_palindrome_permutation(str_input):
    str_input = str_input.lower().replace(' ', '')
    d = dict()
    for i in str_input:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    odd = 0
    for k, v in d.items():
        if v % 2 != 0 and odd == 0:
            odd += 1
        elif v % 2 != 0 and odd != 0:
            return False
    return True


print(is_palindrome_permutation(palim_perm))
print(is_palindrome_permutation(not_palin_perm))
