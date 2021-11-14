# Split list into smaller lists by specifying the number of parts
def split_list(list, parts=1):
    length = len(list)
    return [list[i * length // parts: (i + 1) * length // parts]
            for i in range(parts)]

print(split_list([1,2,3,4,5,6,7,8,9,0]))
# Split list into smaller lists by specifying the number of size
def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs
