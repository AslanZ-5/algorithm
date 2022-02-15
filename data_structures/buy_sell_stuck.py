A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


# Time complexity: O(n^2)
# Space complexity: O(1)
def buy_and_sell(A):
    max_profit = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit


# Time complexity: O(n)
# Space complexity: O(1)
def buy_and_sell_method_2(A):
    max_profit = 0
    min_price = A[0]
    for price in A:
        min_price = min(min_price,price)
        compare_profit = price - min_price
        max_profit = max(compare_profit,max_profit)
    return max_profit
print(buy_and_sell(A))
print(buy_and_sell_method_2(A))