"""
Given two strings, write a method to decide if
one is a permutation of the other.
"""

is_permutation_1 = 'Dogrg'
is_permutation_2 = 'grGod'
not_permutation_1 = 'nOt'
not_permutation_2 = 'top'


def is_perm(st1, st2):
    st1 = st1.lower()
    st2 = st2.lower()

    if len(st1) != len(st2):
        return False
    st1 = ''.join(sorted(st1))
    st2 = ''.join(sorted(st2))
    for i in range(len(st1)):
        if st1[i] != st2[i]:
            return False
    return True


print(is_perm(is_permutation_1, is_permutation_2))
print(is_perm(not_permutation_1, not_permutation_2))


def is_perm_2(st1, st2):
    st1 = st1.lower()
    st2 = st2.lower()

    if len(st1) != len(st2):
        return False

    d = dict()

    for i in st1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in st2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    print(d)
    if all(value == 0 for value in d.values()):
        return True
    else:
        return False


print(is_perm_2(is_permutation_1, is_permutation_2))
print(is_perm_2(not_permutation_1, not_permutation_2))