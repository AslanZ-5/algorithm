# First uppercase later

input_str_1 = 'lucidProgramming'
input_str_2 = 'LucidProgramming'
input_str_3 = 'lucidprogramming'

def inter_s(str_inp):
    for i in str_inp:
        if i.isupper():
            return i
    else:
        return None



def rec_s(str_inp):
    if str_inp[0].isupper():
        return str_inp[0]
    if len(str_inp) < 2:
        return None
    return rec_s(str_inp[1:])

print(inter_s(input_str_3))
print(rec_s(input_str_3))