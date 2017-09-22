# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list.
'''
Use a int array to represent the number, leftest is the highest bit.
Space complexity O(1) - Time complexity O(N)
Like 99, 999, please remember to insert 1 in the leftest position
'''

def plusOne(digits):
    len_s = len(digits)
    carry = 1
    for i in range(len_s - 1, -1, -1):
        total = digits[i] + carry
        digit = int(total % 10)
        carry = int(total / 10)
        digits[i] = digit
    if 1 == carry:
        digits.insert(0,1)
    return digits

n = [9,0,9]
plusOne(n)