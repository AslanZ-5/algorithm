import timeit

"""take an input of n and return the sum of the numbers from 0 to n
"""


def sum1(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def sum2(n):
    return (n * (n + 1)) / 2


start = timeit.timeit()
sum1(100)
end = timeit.timeit()
print('sum1:',end - start)

start = timeit.timeit()
sum2(100)
end = timeit.timeit()
print('sum2:',end - start)


