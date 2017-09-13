# Given a roman numeral, convert it to an integer.(input is from 1 to 3999)
'''
Rules: from left to right, left >= right, so we accumulate them ha.
       but then two neighboring elements， the left < right, we have to substract the left
Space complexity O(N), time complexity O(N)
Mind the case of "IV = 4"
'''

def romanToInt(s):
    digits = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    len_s = len(s)
    num = 0
    for i in range(0, len_s - 1):
        cur = digits[s[i]]
        next = digits[s[i + 1]]
        if cur >= next:
            num += cur
        else:
            num -= cur
    num += digits[s[len_s - 1]]
    return num

n = ["I","V"]
romanToInt(n)