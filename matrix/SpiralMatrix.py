'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
For example,
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

def spiralOrder(matrix):
    m = len(matrix)
    if 0 == m:
        return []
    n = len(matrix[0])
    if 0 == n:
        return []
    arr = []
    round = (min(m,n) + 1) / 2
    for x in range(0, round):
        for y in range(x, n-x):
            arr.append(matrix[x][y])
        for y in range(x+1, m-x-1):
            arr.append(matrix[y][n-x-1])
        if m - 2*x > 1:
            for y in range(n-x-1, x-1, -1):
                arr.append(matrix[m-x-1][y])
        if n - 2*x > 1:
            for y in range(m-x-2, x, -1):
                arr.append(matrix[y][x])
    return arr