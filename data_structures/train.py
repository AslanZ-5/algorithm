a = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


def buy_and_sell_once(a):
    max_profit = 0
    min_price = a[0]
    for price in a:
        min_price = min(price, min_price)
        cur_profit = price - min_price
        max_profit = max(max_profit, cur_profit)
    return max_profit

print(buy_and_sell_once(a))