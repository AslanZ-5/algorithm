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
                a.append((min((i, j)), max((i, j))))
    return '\n'.join(map(str, list(set(a))))


# print(pair_sum([1, 3, 2, 2], 4))


def pair_sum_2(arr, k):
    if len(arr) < 2:
        return print('Too small')
    seen = set()
    output = set()
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    print('\n'.join(map(str, list(output))))


# pair_sum_2([2, 2, 1, 3], 4)


# Largest Subarray Sum Problem
"""Take an array with positive and negative integers and
find the maximum sum of that array"""


def largest(arr):
    if len(arr) == 0:
        return print('too small')
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum


print(largest([-2, -3, 4, -1, -2, 1, 5, -3]))

# How to reverse a String

"""
Given a string of words, reverse all the words
start = 'This is the best'
end = 'best the is This'

"""


def reverse_str1(st):
    return " ".join(reversed(st.split()))

def split_str(st):
    length = len(st)
    spaces = [' ']
    words = []
    i = 0
    while i < length:
        if st[i] not in spaces:
            start = i
            while i < length and st[i] not in spaces:
                i += 1
            words.append(st[start:i])
        i += 1
    return words
def reverse_str(st):
    length = len(st)
    spaces = [' ']
    words = []
    i = 0
    while i < length:
        if st[i] not in spaces:
            start = i
            while i < length and st[i] not in spaces:
                i += 1
            words.append(st[start:i])
        i += 1
    stt = ''
    for i in words[::-1]:
        stt += ' ' + i
    return stt.strip()


st = 'This is the best'
print(split_str(st))
print(reverse_str(st))

print(len(st))
