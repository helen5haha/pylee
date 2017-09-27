# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining
'''
For example:
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
Space complexity O(n); Time complexity O(n)
For a point, the volume it can trap depends on the min of the highest wall on its left and right
'''

def trap(A):
    len_A = len(A)
    if 1 == len_A:
        return 0
    max_heights = [0] * len_A # record the max trapping volume of each point
    left_max = 0
    for i in range(0, len_A): # traverse A from left to right, update max_heights with the encountered max
        if A[i] > left_max:
            left_max = A[i]
        max_heights[i] = left_max
    right_max = 0
    for i in range(len_A - 1, -1, -1): # traverse A from right to left, update max_heights if a smaller value comes in
        if A[i] > right_max:
            right_max = A[i]
        if right_max < max_heights[i]:
            max_heights[i] = right_max
    result = 0
    for i in range(0, len_A): # traverse max_heights, if value is larger than the one in the A, sum it.
        if max_heights[i] > A[i]:
            result += (max_heights[i] - A[i])
    return result

A = [0,1,0,2,1,0,1,3,2,1,2,1]
trap(A)