'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Clue: find the max and min. Max must be right to Min, otherwise it is loss not profit.
Go over all numbers in array, record the min, then calculate the gap of current and the min. Then record the max gap
'''

def maxProfit(prices):
    if None == prices or len(prices) < 2:
        return 0
    min = prices[0]
    max_diff = 0
    for i in range(1, len(prices)):
        if prices[i - 1] < min:
            min = prices[i - 1]
        cur_diff = prices[i] - min #
        if cur_diff > max_diff:
            max_diff = cur_diff
    return max_diff

prices = [2, 4, 6, 1]
maxProfit(prices)