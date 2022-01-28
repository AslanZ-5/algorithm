def convert(item):
    if item is None:
        return None
    t = ''
    b = dict()
    for i in item:
        if i in b:
            b[i] +=1
        else:
            b[i] = 1
    for i,j in b.items():
        t += i + str(j) + "-"
    print(t[:-1])
item = 'aaaaaaaaaaaaa4rtwrefer'
convert(item)
# print(convert(item))
