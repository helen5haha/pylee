'''
Given a set of distinct integers, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

result = []
def doSubsets(S, cur_list, cur_index):
    if cur_index > len(S) - 1:
        result.append(cur_list)
        return
    cur_list0 = cur_list[:]
    cur_list1 = cur_list[:]
    cur_list1.append(S[cur_index])
    doSubsets(S, cur_list0, cur_index + 1)
    doSubsets(S, cur_list1, cur_index + 1)

def subsets(S):
    S.sort()
    doSubsets(S, [], 0)
    return result

test = [1,2,3]
subsets(test)