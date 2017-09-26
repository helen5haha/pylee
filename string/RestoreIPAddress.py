'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
For example:
Given "25525511135",
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
Search, Recursive, Pruning
Note that
1 - Every field cannot be larger than 255
2 - Has and only has 4 fields
3 - When a field is longer than 2, it cannot be started with 0
Pruning condition:
1 - If current char is not the last char
1.1  if the current char append to the existing num, and the new num is not larger than 255
1.1.1  if the num of current fields calculated out is less than 3, then we can consider to append "." to the current prefix,
       to start a new field with current char as its first char
1.1.2  if the current existing num is not 0, then we can consider to append the current char to the num
1.2 otherwise check the num of ".", if it is less than 3, then we can consider to append "." to the current prefix,
       to start a new field with current char as its first char
1.3 otherwise, this branch is invalid
2 - If current char is the last char
2.1 if currently we already have 3 "." and the current field is not "0", and if we append the current char to the current num,
    the new num is not larger than 255, then we can consider to do this.
2.2 if currently we already have 2 ".", the add a new ".", use the current char to be as a new field
2.3 otherwise, this branch is invalid
'''

def doRestoreIpAddresses(prefix, num, s, start, fields):
    if start == len(s) - 1:
        results1 = []
        results2 = []
        if int(num + s[start]) <= 255 and 3 == fields and '0' != num:
            results1 = [prefix + s[start]]
        elif 2 == fields:
            results2 = [prefix + '.' + s[start]]
        return results1 + results2
    if int(num + s[start]) <= 255:
        results0 = []
        results1 = []
        if fields < 3:
            results0 = doRestoreIpAddresses(prefix + '.' + s[start], s[start], s, start + 1, fields + 1)
        if '0' != num:
            results1 = doRestoreIpAddresses(prefix + s[start], num + s[start], s, start + 1, fields)
        return results0 + results1
    elif fields < 3:
        results0 = doRestoreIpAddresses(prefix + '.' + s[start], s[start], s, start + 1, fields + 1)
        return results0
    else:
        return []

def restoreIpAddresses(s):
    if len(s) < 4:
        return []
    return doRestoreIpAddresses(s[0], s[0], s, 1, 0)

s = "25525511135"
restoreIpAddresses(s)