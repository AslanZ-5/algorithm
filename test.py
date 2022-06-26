# binary search

def bin_search(d,target):
    l = 0
    n = len(d) - 1

    while l < n:
        mid = (l + n) // 2
        if d[mid] == target:
            print(d[mid])
            return True
        elif d[mid] < target:
            l = mid + 1
        else:
            n = mid - 1
    print('you fucked up!!!')
    return False

def recursion_bin_search(d,target,l,n):
    if l >= n:
        return False
    mid = (l+n) //2
    if d[mid] == target:
        print(d[mid])
        return True
    elif d[mid] < target:
        return recursion_bin_search(d,target,mid +1,n)
    else:
        return recursion_bin_search(d, target,l,mid -1)



data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
print(bin_search(data,28))
print(recursion_bin_search(data,28,0,len(data)-1))