def array_adv(A):
    further_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= further_reached and further_reached <= last_idx:
        further_reached = max(further_reached, A[i] + i)
        i += 1
    return further_reached >= last_idx


# print(array_adv([3,3,1,0,2,0,3]))
# print(array_adv([3,1,1,0,2,0,3]))

from collections import deque


def precision_increment(a):
    a[-1] += 1
    for i in reversed(range(1,len(a))):
        if a[i] != 10:
            break
        a[i] = 0
        a[i-1] += 1
        if a[0] == 10:
            a[0] = 1
            a.append(0)
    return a
A = [9,8, 9]
print(precision_increment(A))



