from collections import deque
c = [1,2,3,4,5,6,7]
a = deque(c)
a.rotate(-1)
A = list(a)
print(A)
def find_lower(A):
    low = 0
    high = len(A)-1
    while low < high:
        mid = (low + high) //2
        if A[mid] > A[high]:
            low = mid +1
        elif A[mid] <= A[high]:
            high = mid
    return low
print(find_lower(A))