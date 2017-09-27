'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
Note:
The solution is guaranteed to be unique.
Greedy Algorithm:
we keep an array to record the remaining(current + added - to consume) gas for each station.
For a ok route, whatever station car is at, its remaining gas should not be less than 0
'''


def canCompleteCircuit(gas, cost):
    len_remain = len(gas)
    remain = [x for x in gas] # init
    for i in range(0, len_remain):
        remain[i] -= cost[i]
    total = 0
    start = 0
    prefix_min = 0
    prefix_tot = 0
    is_find = False
    for i in range(0, len_remain):
        prefix_tot += remain[i]
        if prefix_tot < prefix_min:
            prefix_min = prefix_tot
        total += remain[i]
        if total < 0:
            start = i + 1
            total = 0
            continue
        elif len_remain - 1 == i and total + prefix_min >= 0:
            is_find = True
            break
    return start if is_find else -1

gas = [1,3,5,1]
cost = [1,1,1,1]
canCompleteCircuit(gas,cost)