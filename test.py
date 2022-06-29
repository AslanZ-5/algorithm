
def iter_len(d):
    t = 0
    for i in d:
        t += 1
    return t

print(iter_len('123456'))

def rec_len(d):
    if d == '':
        return 0
    return 1 + rec_len(d[1:])

print(rec_len('123456'))
