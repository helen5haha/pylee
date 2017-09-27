'''
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
solution: sort the intervals according to their starts, then traverse once to merge the adjacent intervals
'''

class Interval:
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

def merge(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort(lambda x,y: cmp(x.start, y.start))
    new_intervals = []
    last_interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i].start >= last_interval.start and intervals[i].start <= last_interval.end:
            if intervals[i].end >= last_interval.start and intervals[i].end <= last_interval.end:
                pass
            else:
                last_interval.end = intervals[i].end
        else:
            new_intervals.append(last_interval)
            last_interval = intervals[i]
    new_intervals.append(last_interval)

    return new_intervals

i1 = Interval(1,3)
i2 = Interval(2,6)
i3 = Interval(8,10)
i4 = Interval(15,18)

intervals = [i1,i2,i3,i4]
ni = merge(intervals)
ni[0].start, ni[0].end, ni[1].start, ni[1].end, ni[2].start, ni[2].end