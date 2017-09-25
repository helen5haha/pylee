'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note:
You are not suppose to use the library's sort function for this problem.
Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with an one-pass algorithm using only constant space?
Solution: define start and end index. Traverse from left to right, if found 0, then swap with start adn start-=1, if found 2, then swap with end and end-=1
In this way we can make sure that elements < start are all 0, elements > end are all 2
'''

def sortColors(A):
    len_A = len(A)
    if 1 == len(A):
        return
    left = 0
    right = len_A - 1
    i = 0
    while i <= right:
        if 0 == A[i]:
            if left == i:
                i += 1
            else:
                A[left], A[i] = A[i], A[left]
            left += 1
        elif 1 == A[i]:
            i += 1
        else:
            if right == i:
                i += 1
            else:
                A[right], A[i] = A[i], A[right]
            right -= 1

A = [0,2,1,1,2,0,0]
sortColors(A)
print A