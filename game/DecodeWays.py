'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
For example,
Given encoded message "12",it could be decoded as "AB" (1 2) or"L" (12).
The number of ways decoding "12" is 2.
Dynamic Planning problem.
Note to handle the cases about "0": "10","20" is ok. but others with "0" is exception
Plus: For most dynamic planning problems, we can optimize the space complexity:
We don't need to create a n*2 array, instead, we only have to keep two rows, that is to say, 2*2 space
'''

def numDecodings(s):
    if None == s or 0 == len(s) or '0' == s[0]:
        return 0
    solu_arr1 = [0, 1]
    solu_arr2 = [0, 0]
    for i in range(1, len(s) + 1):
        cur_ch = s[i - 1]
        last_ch = s[i - 2] if 1 != i else ''
        if cur_ch >= '1' and cur_ch <= '9':
            solu_arr2[0] = solu_arr1[0] + solu_arr1[1]
        else:
            solu_arr2[0] = 0
        double_ch = last_ch + cur_ch
        if '' == last_ch or '0' == last_ch or int(double_ch) > 26:
            solu_arr2[1] = 0
        else:
            solu_arr2[1] = solu_arr1[0]
        solu_arr1, solu_arr2 = solu_arr2, solu_arr1  # swap

    return solu_arr1[0] + solu_arr1[1]

s = "12"
numDecodings(s)