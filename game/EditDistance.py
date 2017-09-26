# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
# Each operation(insert/delete/replace a character is counterd as 1 step)
# Classical Dynamical Planning. Most DP problems can be optimized for space complexity.

def minDistance(word1, word2):
    if "" == word1 and "" == word2:
        return 0
    elif "" == word1:
        return len(word2)
    elif "" == word2:
        return len(word1)
    len1 = len(word1)
    len2 = len(word2)
    arr1 = [0 for y in range(0, len1 + 1)]
    arr2 = [0 for y in range(0, len1 + 1)]
    arr1[0] = 0
    for y in range(1, len1 + 1):
        arr1[y] = y
    for x in range(1, len2 + 1):
        arr2[0] = x
        for y in range(1, len1 + 1):
            arr2[y] = min(arr1[y - 1] + (0 if (word1[y - 1] == word2[x - 1]) else 1), arr1[y] + 1, arr2[y - 1] + 1)
        tmp = arr1
        arr1 = arr2
        arr2 = tmp
        for y in range(0, len1 + 1):
            arr2[y] = 0
    return arr1[len1]

w1 = "hello"
w2 = "world"
minDistance(w1, w2)