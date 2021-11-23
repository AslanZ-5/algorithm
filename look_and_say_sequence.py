def look_and_say_sequence(n):
    x = []
    c = ''
    inx = 0
    while inx < len(n):
        c += n[inx]
        if inx + 1 < len(n):
            if n[inx + 1] != n[inx]:
                x.append(c)
                c = ''
        else:
            x.append(c)
        inx += 1
    return ''.join([str(len(i)) + i[0] for i in x])


print(look_and_say_sequence('1211'))


def look_and_say_sequence_2(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)
s = '1211'
print(look_and_say_sequence_2(s))
