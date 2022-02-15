A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

def buy_and_sell(A):
    max_profit = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit

print(buy_and_sell(A))