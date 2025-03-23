prices = [7, 2, 1, 5, 6, 4, 8]


def stock_buy_sell(prices):
    n = len(prices)
    max_profit = 0
    buy = 0
    sell = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                # max_proft = max(max_profit, profit)
                if profit> max_profit:
                    max_profit = profit
                    buy = i
                    sell = j
    return max_profit, buy, sell


profit, buy, sell = stock_buy_sell(prices)
print(f"profit: {profit}, buying at: {buy}, selling at: {sell}")
