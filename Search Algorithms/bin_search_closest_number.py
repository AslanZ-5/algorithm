"""
Given an array of sorted integers. We need to find the closest value to the
given number.
Array may contain duplicate values and negative numbers.
Examples:
    Input : arr[] = {1, 2, 3, 4, 5, 6, 6, 7, 8, 9}
    Target number = 11
    Output : 9
    9 is closest to 11 in given array

    Input : arr[] = {2,5,6,7,8,8,9};
    Target  number = 4
    Output : 5
    midpoint: 7
    right of midpoint: 8 -4 = 4
    left of midpoint: 6-4  =2

"""


def find_closest_num(a, target):
    min_diff = float('inf')
    low = 0
    high = len(a) - 1
    closest_num = None

    # Edge cases for empty list or
    # when the list is only one element.
    if len(a) == 0:
        return None
    if len(a) == 1:
        return a[0]

    while low <= high:
        mid = (low + high) // 2
        # Ensure we don't read beyond the bound of the list
        # And obtain the left and right difference values
        if mid + 1 < len(a):
            min_diff_right = abs(a[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(a[mid - 1] - target)

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = a[mid - 1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = a[mid + 1]

        if a[mid] < target:
            low = mid + 1
        elif a[mid] > target:
            high = mid - 1
        else:
            return a[mid]
    return closest_num


a = [2, 6, 7, 8, 8, 9]

print(find_closest_num(a, 4))
