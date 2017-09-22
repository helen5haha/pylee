'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.
Every round, when encounter a different char then stop the count of this round.
Please note that the last round, because it encounters the end of the string, so we have to force stop the round
'''

def doCountAndSay(src):
    char = src[0]
    num = 0
    result = ""
    for c in src:
        if char == c:
            num += 1
        else:
            result += (str(num) + char)
            char = c
            num = 1
    result += (str(num) + char)
    return result

def countAndSay(n):
    if 0 == n:
        return ""
    elif 1 == n:
        return "1"
    result = "1"
    for i in range(1,n):
        result = doCountAndSay(result)
    return result

countAndSay(4)