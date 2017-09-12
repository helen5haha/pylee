'''
Given a sorted array, remove the duplicates in place such that each element appear onlyonce and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
Note the operation on index to avoid removing all later elements everytime
'''

def removeDuplicates(A):
    if None == A:
        return 0
    len_A = len(A)
    if len_A <= 1:
        return len_A
    m = 0
    n = 1
    while n < len_A:
        if A[m] != A[n]:
            m += 1
            if m != n:
                A[m] = A[n]
        n += 1
    return m + 1

A = [1,1,2]
removeDuplicates(A)