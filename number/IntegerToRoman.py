# Given an integer, convert it to a roman numeral.(input is guaranteed to be within the range from 1 to 3999)
'''
Roman cannot represent zero and negative numbers
'''


def intToRoman(num):
    if num <= 0:
        return ""
    nums = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    chs = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    len = 13
    s = ""
    while num > 0:
        for i in range(0, len):
            if num >= nums[i]:
                num -= nums[i]
                s += chs[i]
                break
    return s

intToRoman(4)
