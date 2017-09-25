'''
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
if found the target, then return the index, otherwise return the position it should be inserted
In bisect-search we need to care whether we should return left or right.
In the final, left must be in the target or at the right of the inserted position
'''


def searchInsert(A, target):
    if None == A:
        return 0
    len_A = len(A)
    if target > A[len_A - 1]:
        return len_A
    if target < A[0]:
        return 0

    left = 0
    right = len_A - 1
    while left <= right:  # also can be left < right
        mid = (left + right) / 2
        if A[mid] < target:
            left = mid + 1
        elif A[mid] > target:
            right = mid - 1
        else:
            return mid
    return left

a = [1,3,5,6]
t = 7
searchInsert(a,t)