'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
'''

def doSearch(A, left, right, target):
    len_A = right - left + 1
    if 0 == len_A: ##
        return -1
    elif 1 == len_A: ##
        return left if target == A[left] else -1
    if A[left] < A[right]:
        while left <= right:
            mid = (left + right) / 2
            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid - 1
            else:
                return mid
    else:
        mid = (left + right) / 2
        left_result = doSearch(A, left, mid, target)
        if -1 != left_result:
            return left_result
        else:
            right_result = doSearch(A, mid+1, right, target)
            if -1 != right_result:
                return right_result
    return -1

def search(A, target):
    return doSearch(A, 0, len(A)-1, target)

test = [4,5,6,7,0,1,2]
t = 6
search(test, 6)