'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
Note: m and n will be at most 100
Clue: the permutation formula
'''

def uniquePaths(m, n):
    if 0 == m or 0 == n:
        return 1
    up = 1
    for i in range(m+n-2, n-1, -1):
        up *= i
    down = 1
    for j in range(1, m):
        down *= j
    return up/down


