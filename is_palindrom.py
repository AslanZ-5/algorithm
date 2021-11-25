def is_palindrom(string):
    string = ''.join([i for i in string if i.isalpha()]).lower().replace(' ', '')
    print(string)
    if string == string[::-1]:
        return True
    else:
        return False


def is_palindrom_2(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


print(is_palindrom('was it a cat i saw?'))
print(is_palindrom_2('was it a cat i saw?'))
