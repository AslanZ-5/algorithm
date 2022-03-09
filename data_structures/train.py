# Arbitrary Precision Increment

a = [1,4,9]
a1 = [9,9,9]

# print(int(''.join(map(str,a)))+1)


def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
        if A[0] == 10:
            A[0] = 1
            A.append(0)
    return A

print(plus_one(a))
print(plus_one(a1))