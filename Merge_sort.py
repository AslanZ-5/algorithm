"""

    Divide and Conquer algorithm
        -Break down problem into multiple subproblems recursively until they
         become simple to solve.
        -Solutions are combined to solve original problem.
    O(n*log(n)) running time
        optimal running time for comparison based algorithms


    Merge sort algorithm:
    1. Split array in half
    2. Call Merge Sort on each half to sort them recursively
    3. Merge both sorted halves into one sorted array.

"""

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        print('left =====',left_arr)
        print('right ----',right_arr)
        print(arr)

merge_sort([6,3,2,5,6,9,3,1,0,9])