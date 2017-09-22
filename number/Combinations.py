# Given two integers n and k, return all possible combinations of k numbers out of 1..n
'''
For example,
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

lists = []

def doCombine(list, n, m, k):
    if 0 == k:
        lists.append(list)
        return
    if m > n:
        return
    doCombine(list[:], n, m+1, k)
    new_list = list
    new_list.append(m)
    doCombine(new_list, n, m+1, k-1)

# Return a list of lists of integers
def combine(n,k):
    if k > n:
        return []
    doCombine([], n, 1, k)
    return lists

combine(4,2)