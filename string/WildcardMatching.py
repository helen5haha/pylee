'''
Implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
Dynamic Planning:
Note to handle some special cases
1 - multiple * to be one *
2 - if ? + char > s.length, then return false
'''

def isMatch(s, p):
    if (None == s or '' == s) and (None == p or '' == p):
        return True
    len_s = len(s)
    len_p = len(p)
    new_p = ''
    last_ch = None
    p_solid_char_num = 0
    for i in range(0, len_p):
        if '*' != last_ch or '*' != p[i]:
            new_p += p[i]
        last_ch = p[i]
        if '*' != p[i]:
            p_solid_char_num += 1
    if p_solid_char_num > len_s:
        return False
    if (None == s or '' == s) and 0 == p_solid_char_num:
        return True
    p = new_p
    len_p = len(new_p)

    F = [[False for j in range(0, len_p + 1)] for i in range(0, 2)]

    # 3 cases for True:
    #    last ch matched, and this ch matched (right-down)
    #    p comes *, and last matched (right)
    #    last p.ch is *, s comes any ch, and last matched (down)
    for i in range(1, len_s + 1):
        if 1 == i:
            F[0][0] = True
            for j in range(1, len_p + 1):
                F[0][j] = (F[0][j - 1] and '*' == p[j - 1])
        else:
            for j in range(0, len_p + 1):  # cannot be F[0] = F[1]
                F[0][j] = F[1][j]
        F[1][0] = False
        for j in range(1, len_p + 1):
            if True == F[0][j - 1] and (p[j - 1] == s[i - 1] or '?' == p[j - 1] or '*' == p[j - 1]):
                F[1][j] = True
            elif (True == F[1][j - 1] or True == F[0][j]) and '*' == p[j - 1]:
                F[1][j] = True
            else:
                F[1][j] = False

    return F[1][len_p]

s = "aa"
p = "*"
isMatch(s,p)