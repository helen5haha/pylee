'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
Leverage Stack to simulate the calculation process
'''

def evalRPN(tokens):
    len_tokens = len(tokens)
    if 0 == len_tokens:
        return 0

    # python has no stack, so we have to simulate it
    nums_stack = []

    for i in range(0, len_tokens):
        token = tokens[i]
        # consider negative number, so we shouldn't decide by the first char, but last char
        last_ch = token[len(token) - 1]
        if last_ch >= '0'  and last_ch <= '9':
            nums_stack.append(int(token))
        else:
            right = nums_stack.pop()
            left = nums_stack.pop()
            if '+' == token:
                result = left + right
            elif '-' == token:
                result = left - right
            elif '*' == token:
                result = left * right
            else:
                sign = 1 if (left >= 0 and right >= 0) or (left <= 0 and right <= 0) else -1
                result = abs(left) //abs(right) * sign
            nums_stack.append(result)
    return nums_stack.pop()

t = ["2", "1", "+", "3", "*"]
evalRPN(t)