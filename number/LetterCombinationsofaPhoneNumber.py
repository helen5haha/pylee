# Given a digit string, return all possible letter combinations that the number could represent.
'''
A mapping of digit to letters is given below:
1 - ; 2 - abc; 3 - def; 4 - ghi; 5 - jkl; 6 - mno; 7 - pqrs; 8 - tuv; 9 - wxyz; 0 -
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note: Although the above answer is in lexicographical order, your answer could be in any order you want.
'''


def letterCombinations(digits):
    map = {
        "0": (),
        "1": (),
        "2": ("a", "b", "c"),
        "3": ("d", "e", "f"),
        "4": ("g", "h", "i"),
        "5": ("j", "k", "l"),
        "6": ("m", "n", "o"),
        "7": ("p", "q", "r", "s"),
        "8": ("t", "u", "v"),
        "9": ("w", "x", "y", "z")
    }
    result1 = [""]
    result2 = []
    for ch in digits:
        list = map[ch]
        if 0 == len(list):
            continue
        for str in result1:
            for suffix in list:
                result2.append(str + suffix)
        result1 = result2
        result2 = []
    return result1