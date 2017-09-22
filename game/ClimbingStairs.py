'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Dynamic Planning or just like Fibonacci because f(x) only depends on f(x-1) and f(x-2)
'''

def climbStairs(n):
    if n <= 1:
        return 1
    arr = [1, 1, 0]  # look here, arr[0] = 1, arr[1] = 1
    for i in range(2, n + 1):
        arr[2] = arr[0] + arr[1]
        arr[0], arr[1] = arr[1], arr[2]
    return arr[2]

climbStairs(2)