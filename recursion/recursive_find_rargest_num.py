# find the largest number in a list

def largest_num(ls):
    largest = 0
    for i in ls:
        if i > largest:
            largest = i
    return largest


def largest_num_rec(ls):
    if len(ls) == 2:
        if ls[0] > ls[1]:
            return ls[0]
        else:
            return ls[1]
    left_most = ls[0]

    largest_on_right = largest_num_rec(ls[1:])
    if largest_on_right > left_most:
        return largest_on_right
    else:
        return left_most
