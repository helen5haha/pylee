'''
Follow up for N-Queens problem.
Now, instead outputting board configurations, return the total number of distinct solutions.
'''

paths_count = 0

def totalNQueens(n):
    doTotalNQueens2(n, [], 0)
    return paths_count

def doTotalNQueens2(n, prefix, level):
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
                doTotalNQueens2(n, new_prefix, level + 1)
            else:
                global paths_count
                paths_count += 1

totalNQueens(4)


