data = [2, 3, 4, 5, 67, 12, 13, 41, 54, 76, 5, 59, 765, 34, 54]
data.sort()
print(data)
target = 4
# print(len(data))
# print(12//2)



# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# Iterative Binary Search
def binary_search_tierative(data,target):
    low = 0
    high = len(data) -1

    while low <= high:
        mid = (low + high) //2
        if target == data[mid]:
            print('target' ,data[mid])
            return True
        # if target is smaller than mid ignore right half
        elif target < data[mid]:
            high = mid -1
        # if target is greater than mid ignore left half 
        else:
            low = mid + 1
    return False


print(binary_search_tierative(data,target))