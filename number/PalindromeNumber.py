# Determine whether an integer is a palindrome. Do this without extra space
'''
If you are thinking of converting the integer to string, note the restriction of using extra space.
You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you handle such case?
'''

def isPalindrome(x):
    if x < 0:
        return False
    if x < 10:
        return False
    div = 1
    val = x
    while True:
        val = int(val / 10)
        if val > 0:
            div *= 10
        else:
            break
    while div > 0:
        left = int (x / div)
        right = int(x % 10)
        if left != right:
            return False
        x = x % div
        x = x / 10
        div = int(div / 100)
    return True

x = 0
isPalindrome(x)