# Two Sum Problem



def two_sum(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 20
print(two_sum(A,target))
print(-2+11)