"""
Bubble Sort is a simple sorting algorithm that repeatedly swaps two adjacent elements
through iterations through the list length to create a sort list.
"""


def bubble_sorting(ls):
    inx = len(ls) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(inx):
            if ls[i]> ls[i+1]:
                is_sorted = False
                ls[i],ls[i+1] = ls[i+1] ,ls[i]

ls = [2,1,6,9,3,6,4,0,4,8]

bubble_sorting(ls)
print(ls)


