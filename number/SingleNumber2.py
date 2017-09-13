'''
Given an array of integers, every element appears three times except for one. Find that single one.
Note:Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
An int number has 32 bits, we can use this 32-bit variable to store the occurance of the '1' of the n elements in the array.
And then var mod 3 -> if 1, then this bit represents the bit of the found element in binary is 1
'''

def singleNumber2(A):
    len_A = len(A)
    if len_A <= 3:
        return 0
    counts = [0] * 32
    res = 0
    for i in range(0, 32):
        for num in A:
            counts[i] += (num >> i) & 1
        res |= ((counts[i] % 3) << i)
    if 0 != counts[31] % 3:
        res -= pow(2, 32)
    return res

t = [1,1,1,3,4,4,4]
singleNumber2(t)