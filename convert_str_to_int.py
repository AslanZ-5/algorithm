"""
You are given some numeric string as input. Convert the string you are given to an integer. Do not make use of the built-in "int"
function.

Example:
    "123" -> 123
    "-123455" -> -123455
    "554" -> 554
    etc.
"""

def str_to_int(input_str):
    output_int = 0
    if input_str[0] == '-':
        start_inx = 1
        is_negative = True
    else:
        start_inx = 0
        is_negative = False

    for i in range(start_inx,len(input_str)):
        place = 10 ** (len(input_str) - (i+1))
        digit = ord(input_str[i]) - ord('0')
        output_int += place*digit
    if is_negative:
        return -1 * output_int
    else:
        return output_int

a = '554'
print(str_to_int(a))
