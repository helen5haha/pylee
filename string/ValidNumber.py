'''
Validate if a given string is numeric.
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.
'''


def getType(ch):
    if '^' == ch:
        return 0
    elif ' ' == ch:
        return 1
    elif '+' == ch or '-' == ch:
        return 2
    elif ch >= '0' and ch <= '9':
        return 3
    elif '.' == ch:
        return 4
    elif 'e' == ch:
        return 5
    elif '$' == ch:
        return 6
    else:
        return 7


def getMap():
    map = (
        (0, 0, 1, 4, 2, -1, -1, -1),  # 0: ^ / space
        (-1, -1, -1, 4, 2, -1, -1, -1),  # 1: + / -
        (-1, -1, -1, 3, -1, -1, -1, -1),  # 2: .
        (-1, 10, -1, 3, -1, 7, 11, -1),  # 3: num
        (-1, 10, -1, 4, 5, 7, 11, -1),  # 4: num
        (-1, 10, -1, 6, -1, 7, 11, -1),  # 5: .
        (-1, 10, -1, 6, -1, 7, 11, -1),  # 6: num
        (-1, -1, 8, 9, -1, -1, -1, -1),  # 7: e
        (-1, -1, -1, 9, -1, -1, -1, -1),  # 8: + / 1
        (-1, 10, -1, 9, -1, -1, 11, -1),  # 9: num
        (-1, 10, -1, -1, -1, -1, 11, -1)  # 10: space
    )
    return map


def isNumber(s):
    map = getMap()
    state = 0
    after_s = "^" + s + "$"
    for ch in after_s:
        type = getType(ch)
        state = map[state][type]
        if -1 == state:
            break
    return 11 == state

isNumber("2e10")