'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as[1,5],[6,9].
Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as[1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
First to find the location of newInterval in the current array, there are 3 possibilities:
1 - newInterval not overlaps with the current array, and be the leftest(left_index=0, right_index=-1)
2 - newInterval not overlaps with the current array, and be the rightest(left_index=-1)
3 - newInterval overlaps with the current array:
    left_index represents the max interval in the current array, whose end >= newInterval's start
    right_index represents the min interva in the current array, whose start <= newInterval's end
For all the impacted intervals, we need to merge them with newInterval to a single interval.
For all the unimpacted intervals, we do nothing, just add them back to the result array.
'''
class Interval:
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

def insert(intervals, newInterval):
    len_intervals = len(intervals)
    if 0 == len_intervals:
        return [newInterval]

    left_index = -1
    right_index = -1
    find_left = False
    for m in range(0, len_intervals):
        if not find_left and newInterval.start <= intervals[m].end:
            find_left = True
            left_index = m
        if find_left:
            if newInterval.end >= intervals[m].start:
                right_index = m

    if -1 == left_index:  ###
        intervals.append(newInterval)
        return intervals
    new_intervals = []
    for m in range(0, left_index):
        new_intervals.append(intervals[m])
    add_interval = None
    start_index = -1
    if -1 != right_index:
        add_interval = Interval(min(newInterval.start, intervals[left_index].start),  max(newInterval.end, intervals[right_index].end))
        start_index = right_index + 1
    else:  ###
        add_interval = newInterval
        start_index = left_index
    new_intervals.append(add_interval)
    for m in range(start_index, len_intervals):
        new_intervals.append(intervals[m])

    return new_intervals

i1 = Interval(1,3)
i2 = Interval(6,9)
i3 = Interval(2,5)
intervals = [i1,i2]

ni = insert(intervals, i3)
ni[0].start, ni[0].end, ni[1].start, ni[1].end