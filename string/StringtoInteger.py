'''
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases.
Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''

max_int_bits = 32
max_int_str = str(pow(2, max_int_bits - 1) - 1)
min_int_str = str(pow(2, max_int_bits - 1))  # abs value, without sign
max_int_len = len(max_int_str)
min_int_len = len(min_int_str)

def atoi(str):
    len_s = len(str)
    if 0 == len_s:
        return 0

    index = 0
    while index < len_s and ' ' == str[index]:
        index += 1
    sign = 1
    if index < len_s:
        if '+' == str[index]:
            sign = 1
            index += 1
        elif '-' == str[index]:
            sign = -1
            index += 1
    value = 0
    val_str = ''
    for i in range(index, len_s):
        ch = str[i]
        if ch >= '0' and ch <= '9':
            val_str += ch

            if len(val_str) > max_int_len or len(val_str) > min_int_len:
                return int(max_int_str) if 1 == sign else -int(min_int_str)
            if len(val_str) >= max_int_len and val_str > max_int_str:
                return int(max_int_str) if 1 == sign else -int(min_int_str)

            value = value * 10 + ord(ch) - ord('0')
            index += 1
        else:
            break

    return value * sign

atoi("1234")



