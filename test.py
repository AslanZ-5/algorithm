# Given a string, find the first uppercase character.
# Solve using both an iterative and recursive solution.

input_str_1 = "lucidProgramming"
input_str_2 = "Lucidrogramming"
input_str_3 = "lucidprogramming"


def find_upper(st):
    for i in st:
        if i.isupper():
            print(i)
            return True
    return False

# print(find_upper(input_str_1))


def find_upper_rec(st,inx=0):
    if st[inx].isupper():
        print(st[inx])
        return True
    if inx == len(st) -1:
        return False
    return find_upper_rec(st,inx+1)

print(find_upper(input_str_3))

print('----------rec')
print(find_upper_rec(input_str_3))
