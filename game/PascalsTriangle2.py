'''
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].
Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

def getRow(rowIndex):
    if rowIndex <= 0:
        return [1]
    elif 1 == rowIndex:
        return [1,1]
    elif rowIndex >= 2:
        need_rowsnum = rowIndex - 1
        last_row = [1,1]
        for i in range(0, need_rowsnum):
            new_row = [1]
            for j in range(1, len(last_row)):
                new_row.append(last_row[j - 1] + last_row[j])
            new_row.append(1)
            last_row = new_row
        return last_row

getRow(3)