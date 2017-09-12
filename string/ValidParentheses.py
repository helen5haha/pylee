# Given a string containing just the characters '(', ')','{','}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but"(]" and"([)]" are not.

def isMatch(l, r):
    return ("(" == l and ")" == r) or ("[" == l and "]" == r) or ("{" == l and "}" == r)

def isValid(s):
    len_s = len(s)
    if 0 == len_s:
        return True
    arr = []
    for ch in s:
        len_arr = len(arr)
        if 0 == len_arr or not isMatch(arr[len_arr - 1], ch):
            arr.append(ch)
        else:
            arr.pop()
    return 0 == len(arr)

s = "()(()}"
isValid(s)

