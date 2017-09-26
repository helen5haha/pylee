# Write a function to find the longest common prefix string amongst an array of strings

def findPrefix(str1, str2):
    min_len = min(len(str1), len(str2))
    for i in range(0, min_len):
        if str1[i] != str2[i]:
            return str1[0:i]
    return str1[0:min_len]

def longestCommonPrefix(strs):
    if None == strs:
        return ""
    n = len(strs)
    if 0 == n:
        return ""
    elif 1 == n:
        return strs[0]

    prefix = strs[0]
    for str in strs[1:]:
        prefix = findPrefix(prefix, str)
        if "" == prefix:
            break
    return prefix

s1 = "adddress"
s2 = "address"
s = [s1,s2]
longestCommonPrefix(s)