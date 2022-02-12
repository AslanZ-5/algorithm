def array_adv(A):
    further_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= further_reached and further_reached <= last_idx:

        further_reached = max(further_reached, A[i] + i)
        i += 1
    return further_reached >= last_idx

print(array_adv([3,3,1,0,2,0,3]))
print(array_adv([3,1,1,0,2,0,3]))