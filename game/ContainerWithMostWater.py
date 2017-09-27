'''
Given n non-negative integers a1, a2, ...,an, where each represents a point at coordinate (i,ai).
n vertical lines are drawn such that the two endpoints of line i is at (i,ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container.
Use two pointers, start search from left and right, to the middle
'''

def maxArea(height):
    len_height = len(height)
    if 1 == len_height:
        return 0
    max_area = 0
    left_index = 0
    right_index = len_height - 1
    while left_index < right_index:
        if height[left_index] < height[right_index]:
            area = (right_index - left_index) * height[left_index]
            left_index += 1
        else:
            area = (right_index - left_index) * height[right_index]
            right_index -= 1
        if area > max_area:
            max_area = area
    return max_area

h = [1,3,5,1]
maxArea(h)

