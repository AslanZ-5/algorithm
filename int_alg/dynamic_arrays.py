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


# print(largest([-2, -3, 4, -1, -2, 1, 5, -3]))

# How to reverse a String

"""
Given a string of words, reverse all the words
start = 'This is the best'
end = 'best the is This'

"""


def reverse_str1(st):
    return " ".join(reversed(st.split()))


def split_str(st, t=' '):
    length = len(st)
    spaces = [t]
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


"""
    Given 2 arrays (assume no duplicates)
    is 1 array a rotation of another - return True/False
    same size and elements but start index is different 
    
    Big O(n) we are going through each array 2x but O(2n) = O(n) since infinite sized lists,
    constants means nada
    
    select an indexed position in list1 and gets its value. Find same element in list2 and check index for index from there 
    if any variation then we know its false.
    Getting to last item without a false means true.
"""


def rotation_arr(list1, list2):
    if len(list1) != len(list2):
        return False
    key = list1[0]
    key_index = 0
    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i
            break
    if key_index == 0:
        return False

    for i in range(len(list1)):
        list2inx = (key_index + i) % len(list1)

        if list1[i] != list2[list2inx]:
            return False
    return True


# a = [0, 0, 0, 4, 5, 6, 7]
# b = [4, 5, 6, 7, 0, 0, 0]
#
# print(rotation_arr(a, b))

# Array Common Elements
"""
Common Elements in Two Sorted Arrays 
return the common elements (as an array) between two sorted arrays of integers (ascending order).
Example: The common elements between [1,3,4,6,7,9] and [1,2,4,5,9,10]
are [1,4,9]

"""


def common_element(ls1, ls2):
    p1 = 0
    p2 = 0
    result = []

    while p1 < len(ls1) and p2 < len(ls2):
        if ls1[p1] == ls2[p2]:
            result.append(ls1[p1])
            p1 += 1
            p2 += 1
        elif ls1[p1] > ls2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result


# print(common_element([1,3,4,6,7,9] , [1,2,4,5,9,10]))


# Mine Sweeper
"""
    Write a function that will take 3 arguments:
    bombs = list of bomb locations
    rows, columns
    mine_sweeper([[0,0],[1,2]],3,4)
    bomb at row index 0 column index 0
    bomb at row index 0 column index 1
    3 rows 
    4 columns
"""


def mine_sweeper(bombs, num_rows, num_columns):
    field = [[0] * num_columns for i in range(num_rows)]
    for i in bombs:
        row_loc, colm_loc = i
        field[row_loc][colm_loc] = -1

        row_range = range(row_loc - 1, row_loc + 2)
        colm_range = range(colm_loc - 1, colm_loc + 2)
        for i in row_range:
            c = i
            for j in colm_range:
                if 0 <= i < num_rows and 0 <= j < num_columns and field[i][j] != -1:
                    field[i][j] += 1
    return field


# print(mine_sweeper([[0, 0], [1, 2]], 3, 4))


# Frequent Count

"""
 Given an array what is the most frequently occuring element 
"""

def freq_count(lst):
    dt = dict()
    max_count = 0
    max_item = None
    for i in lst:
        if i in dt:
            dt[i] += 1
        else:
            dt[i] = 1
        if dt[i] > max_count:
            max_count = dt[i]
            max_item = i
    return max_item
print(freq_count([1,2,3,4,5,6,6,5,4,45,5,6,7,7,8,9,7,6,5]))