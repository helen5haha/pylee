'''
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
Use string to simulate the binary number add. Change radix to 8 can do the octal add
'''

radix = 2

def addBinary(a,b):
    a_nums = [(ord(ch) - ord('0')) for ch in a]
    b_nums = [(ord(ch) - ord('0')) for ch in b]
    a_nums_size = len(a_nums)
    b_nums_size = len(b_nums)
    max_nums_size = max(a_nums_size, b_nums_size)
    a_extend_nums = [0 for i in range(0, max_nums_size - a_nums_size)]
    b_extend_nums = [0 for i in range(0, max_nums_size - b_nums_size)]
    a_nums = a_extend_nums + a_nums
    b_nums = b_extend_nums + b_nums
    sum_nums = [0] * max_nums_size

    carry = 0
    for i in range(max_nums_size - 1, -1, -1):
        sum = a_nums[i] + b_nums[i] + carry
        sum_nums[i] = sum % radix
        carry = sum / radix
    sum_str = ("1" if 1 == carry else "")
    for i in range(0, max_nums_size):
        sum_str += chr(sum_nums[i] + ord('0'))

    return sum_str

a = "11"
b = "1"
addBinary(a,b)