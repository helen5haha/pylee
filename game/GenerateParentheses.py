'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"
Classical recursive backtracking problem:
left-right matching rule: traverse from left to right, num('(') >= num(')')
SO, in every recursive layer, there are two options(add '(' or add ')')
Whether a branch is to be continued, depends on whether it satisfied the above rule.
left_count: in current recursive layer, number of '('s that already occurred
left_remain: number of '('s that can be used. It is equal to current '(' minus ')'
'''

def doGenerateParenthesis(n, left_count, left_remain, prefix):
    # only one out-point: the string has been finished.
    if n == left_count and 0 == left_remain:
        return [prefix]

    left_list = []
    right_list = []
    if left_count < n:
        left_list = doGenerateParenthesis(n, left_count + 1, left_remain + 1, prefix + "(")
    if left_remain > 0:
        right_list = doGenerateParenthesis(n, left_count, left_remain - 1, prefix + ")")

    return left_list + right_list

def generateParenthesis(n):
    if 0 == n:
        return []
    else:
        list = doGenerateParenthesis(n, 0, 0, "")
        return list

generateParenthesis(3)