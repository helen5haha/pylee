'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again)
We adopt the greedy idea of "buy low and sell high". We need find every incremented subsequence to make the profit maximum.
'''

def maxProfit2(prices):
    len_prices = len(prices)
    if len_prices <= 1:
        return 0

    start = prices[0]
    index = 1
    income = 0
    total_income = 0
    while index < len_prices:
        cur = prices[index]
        if cur >= prices[index - 1]:
            income = cur - start
            index += 1
            if len_prices == index:
                total_income += income
        else:
            total_income += income
            income = 0
            start = cur
            index += 1

    return total_income

prices = [2, 4, 6, 1]
maxProfit2(prices)