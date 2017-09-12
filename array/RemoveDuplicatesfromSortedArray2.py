'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?
For example,
Given sorted array nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
'''

def removeDuplicates2(A):
    if None == A:
        return 0
    len_A = len(A)
    if len_A <= 1:
        return len_A
    m = 0
    n = 1
    count = 1  ##
    while n < len_A:
        if A[m] != A[n]:
            count = 1
            m += 1
            if m != n:
                A[m] = A[n]
        elif count >= 2:
            count += 1
        else:
            m += 1
            count += 1
            if m != n:
                A[m] = A[n]
        n += 1
    A = A[0:m+1] # A must be modified
    return m + 1

A = [1,1,1,2,2,3]
removeDuplicates2(A)