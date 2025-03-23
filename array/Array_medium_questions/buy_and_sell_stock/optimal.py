prices = [7, 2, 1, 5, 6, 4, 8]


def stock_buy_sell(prices):
    n = len(prices)
    mini = float("inf")
    max_profit = 0
    for i in range(0, n):
        mini = min(mini, prices[i])
        max_profit = max(mini, prices[i] - mini)
        return max_profit


print(f"{stock_buy_sell(prices)}")
