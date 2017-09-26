# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
'''
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where'Q' and '.' both indicate a queen and an empty space respectively.
For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Classical backtracking
'''

paths = []

def doSolveNQueens(n, prefix, level):
    for i in range(0, n):
        is_valid = True
        for m in range(0, len(prefix)):
            if i == prefix[m]:
                is_valid = False
                break
            if level - m == i - prefix[m] or level - m == prefix[m] - i:
                is_valid = False
                break
        if is_valid:
            new_prefix = prefix[:]
            new_prefix.append(i)
            if n - 1 != level:
                doSolveNQueens(n, new_prefix, level + 1)
            else:
                paths.append(new_prefix)

def solveNQueens(n):
    doSolveNQueens(n, [], 0)
    lists = []
    for path in paths:
        list = []
        for num in path:
            str = "." * num + "Q" + "." * (n - num - 1)
            list.append(str)
        lists.append(list)
    return lists

solveNQueens(4)