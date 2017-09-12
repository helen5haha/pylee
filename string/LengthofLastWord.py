'''
Given a string s consists of upper/lower-case alphabets and empty space characters' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
For example,
Given s = "Hello World",
return 5.
Please mind some cases like the boundaries, the empty string or the apace after the last word.
'''

def lengthOfLastWord(s):
    len_s = len(s)
    if 0 == len_s:
        return 0

    index = len_s - 1
    while index >= 0 and ' ' == s[index]:
        index -= 1
    len_last_word = 0
    while index >= 0 and ' ' != s[index]:
        len_last_word += 1
        index -= 1
    return len_last_word

s = "i am groot "
lengthOfLastWord(s)