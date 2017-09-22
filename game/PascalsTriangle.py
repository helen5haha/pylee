'''
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def generate(numRows):
    rows = []
    if numRows <= 0:
        return rows
    if numRows >= 1:
        rows.append([1])
    if numRows >= 2:
        rows.append([1,1])
    if numRows >= 3:
        need_rowsnum = numRows - 2
        last_row = [1,1]
        for i in range (0, need_rowsnum):
            new_row = [1]
            for j in range(1, len(last_row)):
                new_row.append(last_row[j-1] + last_row[j])
            new_row.append(1)
            rows.append(new_row)
            last_row = new_row
    return rows

generate(5)