a = 'fairy tales'
b = 'rail safety'
# print(sorted(a) == sorted(b))


def is_anagram1(s1, s2):
    s1 = s1.lower().replace(' ', '')
    s2 = s2.lower().replace(' ', '')
    if len(s1) != len(s2):
        return False
    ht = dict()
    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] != 0:
            return False
    return True



print(is_anagram1(a, b))
