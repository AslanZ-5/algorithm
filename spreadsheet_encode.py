# print(ord('A')-ord('A')+1)
a = 'BC'
c = 'AA'
b = 'ZZ'


def spreadsheet_encode_column(col_str):
    count = len(c) - 1
    sum = 0
    for i in col_str:
        sum += (ord(i) - ord('A') + 1) * 26 ** count
        count -= 1
    return sum
print(spreadsheet_encode_column(b))
