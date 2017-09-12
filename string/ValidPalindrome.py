'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
'''

def isPalindrome(s):
    len_s = len(s)
    if len_s <= 1:
        return True

    left_idx = 0
    right_idx = len_s - 1
    is_match = True
    while left_idx < right_idx:

        if (False == ((s[left_idx] >= 'a' and s[left_idx] <= 'z') or (s[left_idx] >= 'A' and s[left_idx] <= 'Z')  or (s[left_idx] >= '0' and s[left_idx] <= '9'))):
            left_idx += 1
            continue
        left_chr = (chr(ord(s[left_idx]) - ord('A') + ord('a')) if (s[left_idx] >= 'A' and s[left_idx] <= 'Z') else s[left_idx])

        if (False == ((s[right_idx] >= 'a' and s[right_idx] <= 'z') or (s[right_idx] >= 'A' and s[right_idx] <= 'Z') or (s[right_idx] >= '0' and s[right_idx] <= '9'))):
            right_idx -= 1
            continue
        right_chr = (chr(ord(s[right_idx]) - ord('A') + ord('a')) if (s[right_idx] >= 'A' and s[right_idx] <= 'Z') else s[right_idx])

        if left_chr == right_chr:
            left_idx += 1
            right_idx -= 1
        else:
            is_match = False
            break

    return is_match

s = "A man, a plan, a canal: Panama"
isPalindrome(s)