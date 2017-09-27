# Given an array of integers, find two numbers such that they add up to a specific target number
'''
The function should return indices of the two numbers where index1 must be less than index2
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
Note that the array index starts from 1 instead of 0
'''

class Item:
    def __init__(self, value, index):
        self.value = value
        self.index = index

def twoSum(num, target):
    len_num = len(num)
    if 0 == len_num:
        return (-1, -1)

    items = [Item(value, 0) for value in num]
    for i in range(0, len_num):
        items[i].index = i + 1
    items.sort(lambda x, y: cmp(x.value, y.value))
    index1 = 0
    index2 = len_num - 1
    is_find = False
    while index1 < index2:
        total = items[index1].value + items[index2].value
        if total < target:
            index1 += 1
        elif total > target:
            index2 -= 1
        else:
            is_find = True
            break
    (index1, index2) = (index1, index2) if items[index1].index <= items[index2].index else (index2, index1)
    return (items[index1].index, items[index2].index) if is_find else (-1, -1)

numbers = [2, 7, 11, 15]
target = 9
twoSum(numbers, target)

