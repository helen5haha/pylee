'''
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
Greedy Algorithm:
Initialize an array with size N, all elements are 1, indicating every has at least one candy.
Then perform two round greedy processes:
First traverse from left to right, if one ranks higher than its left, then it has one more candy than its left
Second traverse from right to left, if one ranks higher than its right, then it has at least one more candy than its right.
(If one already has more candies than its right, then we need to do nothing)
'''

def candy(ratings):
    len_r = len(ratings)
    if len_r <= 1:
        return len_r
    candys = [1] * len_r
    candys[0] = 1
    candys[len_r - 1] = 1
    for i in range(1, len_r):
        if ratings[i] > ratings[i - 1]:
            candys[i] = candys[i - 1] + 1
    for i in range(len_r - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candys[i] = max(candys[i + 1] + 1, candys[i])
    return sum(candys)

r = [1,2,3,4]
candy(r)