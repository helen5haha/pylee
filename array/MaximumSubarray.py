'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

def maxSubArray(A):
    len_A = len(A)
    if 1 == len_A:
        return A[0]

    max = None
    sum = 0

    for n in range(0, len_A):
        sum += A[n]
        if None == max or sum > max:
            max = sum
        if sum < 0:
            sum = 0
            continue
    return max

A = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(A)
