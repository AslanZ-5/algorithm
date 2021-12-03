data = [2, 3, 4, 5, 67, 12, 13, 41, 54, 76, 5, 59, 765, 34, 54]
data.sort()
print(data)
target = 6
# print(len(data))
# print(12//2)



# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# Iterative Binary Search
def binary_search_iterative(data,target):
    low = 0
    high = len(data) -1

    while low <= high:
        mid = (low + high) //2

        if target == data[mid]:
            print('iter-target' ,data[mid])
            return True
        # if target is smaller than mid ignore right half
        elif target < data[mid]:
            high = mid -1
        # if target is greater than mid ignore left half
        else:
            low = mid + 1
    return False





# Recursive Binary Search
def binary_search_recursive(data,target,low,high):
    if low>high:
        return False
    else:
        mid = (low + high) // 2
        # if target is the middle itself
        if target == data[mid]:
            print('recursive-target',data[mid])
            return True
        # if element is smaller than mid, then it can only
        # be present in left subarray
        elif target < data[mid]:
            return binary_search_recursive(data,target,low,mid-1)
        # Else the element can only be present in right subarray
        else:
            return binary_search_recursive(data,target,mid+1,high)

