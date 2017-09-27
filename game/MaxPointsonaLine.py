# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''
Overall complexity is O(n^2)
Calculate Slope:
Every time we select a point and traverse others, calculate their slopes and add the result to map.
(map in Python is implemented with Hash, so the complexity for insert and search is O(1))
Please take care to handle the two cases:
1 - the point overlaps with the current point. This point can be included to lines with any slopes
2 - the point is vertical to the current point. Because slope is extremly large, we cannot do the divide. Have to handle it exclusively
'''

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def maxPoints(points):
    len_points = len(points)
    if len_points <= 1:
        return len_points
    max_count = 0
    for index1 in range(0, len_points):
        p1 = points[index1]
        gradients = {}
        infinite_count = 0
        duplicate_count = 0
        for index2 in range(index1, len_points):
            p2 = points[index2]
            dx = p2.x - p1.x
            dy = p2.y - p1.y
            if 0 == dx and 0 == dy:
                duplicate_count += 1
            if 0 == dx:
                infinite_count += 1
            else:
                g = float(dy) / dx  # take care
                # seem like cannot do gradients[g] += 1 if key: g not exists
                gradients[g] = (gradients[g] + 1 if gradients.has_key(g) else 1)
        if infinite_count > max_count:
            max_count = infinite_count
        for k, v in gradients.items():
            v += duplicate_count
            if v > max_count:
                max_count = v
    return max_count

p1 = Point(0,0)
p2 = Point(1,1)
p3 = Point(2,2)
p4 = Point(0,0)
p5 = Point(0,3)
points = [p1,p2,p3,p4,p5]
maxPoints(points)
