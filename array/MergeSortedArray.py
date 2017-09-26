'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.
Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
The number of elements initialized in A and B are m and n respectively.
Start from the end to avoid the frequent movement of elements
'''

def merge(A, m, B, n):
    if 0 == n:
        return A
    if 0 == m:
        for i in range(0, n):
            A[i] = B[i]
        return A

    index = m + n - 1
    indexA = m - 1
    indexB = n - 1
    while indexA >= 0 and indexB >= 0:
        if A[indexA] >= B[indexB]:
            A[index] = A[indexA]
            index -= 1
            indexA -= 1
        else:
            A[index] = B[indexB]
            index -= 1
            indexB -= 1
    if indexA >= 0:
        pass
    else:
        for i in range(0, indexB + 1):
            A[i] = B[i]


A = [1,3,5]
B = [2,4]
merge(A, 3, B, 2)
print(A)