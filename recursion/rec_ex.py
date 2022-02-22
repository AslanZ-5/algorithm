def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


# print(factorial(5))


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(8))


# Binary Search

def bin_search(arr, num, left, right):
    mid = (left + right) // 2
    if left > right:
        return -1
    elif arr[mid] == num:
        return mid
    elif arr[mid] < num:
        return bin_search(arr, num, mid + 1, right)
    elif arr[mid] > num:
        return bin_search(arr, num, mid, mid - 1)


arr = [1, 2, 3, 4, 5, 6]


# print(bin_search(arr,6,0,len(arr)-1))


def func(n):
    if n == 1:
        print('end', 1)
    else:
        print(n)
        func(n - 1)
        print(n)


# func(4)

def func2(n):
    if n == 1:
        print(1)
    else:
        func2(n - 1)
        print(n)
        func2(n - 1)


# func2(4)


# recursive Tree

def waysToClimb(n, possibleSteps):
    if n == 0:
        return 1
    nbways = 0
    for steps in possibleSteps:
        if (n - steps) >= 0:
            nbways += waysToClimb(n - steps, possibleSteps)
    return nbways
# print(waysToClimb(10,[2,4,5,8]))

# Visualising recursive tree

def mergeSort(arr,callStack):
    callStack.append(f'megeSort("{str(arr)}")')
    print(callStack)
    if len(arr) < 2:
        callStack.pop()
        print(callStack)
        return arr
    else:
        mid = len(arr) // 2
        leftpart = mergeSort(arr[:mid],callStack)
        rightpart = mergeSort(arr[mid:],callStack)
        callStack.pop()
        print(callStack)

mergeSort([4,5,1,9,2,5,3,4],[])