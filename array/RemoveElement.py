'''
Given an array and a value, remove all instances of that value in place and return the new length.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Solution: put the elements to delete to the end, use m and n, m for traversing from left to right,
n for recording the position from right end that can be swapped
'''

def removeElement(A, elem):
    if None == A:
        return 0
    len_A = len(A)
    m = 0
    n = len_A - 1
    while m <= n:
        if elem == A[m]:
            if elem != A[n]:
                A[m], A[n] = A[n], A[m]
                m += 1
                n -= 1
            else:
                n -= 1
        else:
            m += 1
    return n+1

A = [3, 19, 5, 1, 16]
removeElement(A, 1)