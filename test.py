data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 33, 37]


def binary_search(target, data):
    f = 0
    l = len(data) - 1
    while f <= l:
        mid = (l + f) // 2
        if data[mid] == target:
            print('found')
            return True
        elif data[mid] < target:
            f = mid + 1
        elif data[mid] > target:
            l = mid - 1


binary_search(33, data)


def binary_search_rec(target, data, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            return binary_search_rec(target, data, low, high=mid-1)
        else:
            return binary_search_rec(target, data, mid+1, high)

print(binary_search_rec(27,data,low=0, high=len(data)-1))