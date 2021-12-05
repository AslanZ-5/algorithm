def single_list(a):
    x = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            x.append(a[i][j])


# remove duplicate
def remover(ls):
    a = []
    for i in ls:
        if i not in a:
            a.append(i)
    return a


from itertools import product, permutations, combinations

a = [12, 9, 3, 4, 7, 6]
target = 13
for i in range(len(a)):
    for j in range(len(a)):
        for x in range(len(a)):
            if i != j != x != i:
                if (a[i] + a[j] + a[x]) == target:
                    print(a[i] , '+' ,a[j] , '+' , a[x],'==',target)


rt = [1,2,3,4,5]
t = 1
for i in rt:
    t = t* i
print(t)