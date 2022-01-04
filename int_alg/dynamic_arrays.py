# Anagram
def anagram(s1, s2):
    # Reomove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)


def is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count_dict = dict()

    for i in s1:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    for i in s2:
        if i in count_dict:
            count_dict[i] -= 1
        else:
            count_dict[i] = 1

    for i in count_dict:
        if count_dict[i] != 0:
            return False
    return True


# Array Pair Sum
"""
Given an integer array, output all the unique pairs that sum up to a specific value k.
So the input:
pair_sum([1,3,2,2],4) 
would return 2 pairs:
(1,3)
(2,2)
"""


def pair_sum(arr, sm):
    a = []
    for i in arr:
        for j in arr:
            if i + j == sm:
                a.append((min((i, j)),max((i,j))))
    return '\n'.join(map(str,list(set(a))))


print(pair_sum([1, 3, 2, 2], 4))


def pair_sum_2(arr,k):
    if len(arr) < 2:
        return print('Too small')
    seen = set()
    output = set()
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
    print ('\n'.join(map(str,list(output))))

pair_sum_2([2,2,1,3],4)