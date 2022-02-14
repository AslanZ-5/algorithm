# Given a sorted array of integers, return the two numbers such that
# they add up to a specific target. You may assume that each input
# would have exactly one solution, and you may not use the same element twice.


def two_sum_brute_force(A, target):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False


def two_sum_hash_table(A, target):
    hs = dict()
    for i in range(len(A)):
        if A[i] in hs:
            print(hs[A[i]],A[i])
            return True
        else:
            hs[target - A[i]] = A[i]
    return False
A = [-2, 1, 2, 4, 7, 11]
target = 11
# print(two_sum_brute_force(A, target))
print(two_sum_hash_table(A,target))
