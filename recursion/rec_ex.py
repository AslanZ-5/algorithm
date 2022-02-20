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

def bin_search(arr,num,left,right):
    mid = (left + right) // 2
    if left > right:
        return -1
    elif arr[mid] == num:
        return mid
    elif arr[mid] < num:
        return bin_search(arr,num,mid+1,right)
    elif arr[mid] > num:
        return bin_search(arr,num,mid,mid-1)

arr = [1,2,3,4,5,6]
# print(bin_search(arr,6,0,len(arr)-1))


def func(n):
    if n == 1:
        print('end',1)
    else:
        print(n)
        func(n-1)
        print(n)

# func(4)

def func2(n):
    if n == 1:
        print(1)
    else:
        func2(n-1)
        print(n)
        func2(n-1)

func2(4)