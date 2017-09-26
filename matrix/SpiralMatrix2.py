'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
For example,
Given n = 3,
You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

def generateMatrix(n):
    if 0 == n:
        return [ ]
    m = n
    index = 1
    matrix = [[0 for x in range(0,n)] for y in range(0,n)]
    round = (n+1)/2
    for x in range(0, round):
        for y in range(x, n-x):
            matrix[x][y] = index
            index += 1
        for y in range(x+1, m-x-1):
            matrix[y][n-x-1] = index
            index += 1
        if m - 2*x > 1:
            for y in range(n-x-1, x-1, -1):
                matrix[m-x-1][y] = index;
                index += 1
        if n - 2*x > 1:
            for y in range(m-x-2, x, -1):
                matrix[y][x] = index
                index += 1
    return matrix