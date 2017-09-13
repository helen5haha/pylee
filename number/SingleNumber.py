'''
Given an array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Use XOR operation
'''

def singleNumber(A):
    len_A = len(A)
    if 0 == len_A:
        return 0
    elif 1 == len_A:
        return A[0]
    else:
        result = A[0]
        for i in range(1, len_A):
            result ^= A[i]
    return result

A = [1]
singleNumber(A)