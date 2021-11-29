
def intersection_sorted_array(lst1,lst2):
    i = 0
    j = 0
    intersection = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]:
            if i==0 or lst1[i] != lst1[i-1]:
                intersection.append(lst1[i])
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            i += 1
        else:
            j += 1
    return intersection



print(intersection_sorted_array([2,3,3,5,7,11],[3,3,7,15,31]))