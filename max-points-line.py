# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3

# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4

# Constraints:

# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.


from collections import defaultdict

def maxPoints(points):
    if len(points) < 3:
        return len(points)
    
    # Helper function to find the great common divisor of the two number
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # Find the slope
    def slope(p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        if dx == 0:
            return float('inf')
        elif dy == 0:
            return 0
        else:
            divisor = gcd(dx, dy)
            return (dx // divisor, dy // divisor)
        
    max_points = 0

    for i, point1 in enumerate(points):
        # Create hashmap to store the slope
        slopes = defaultdict(int)
        same_point_count = 0
        current_max = 0

        for j, point2 in enumerate(points):
            # skiip if encounter the same points
            if i != j:
                if point1 == point2:
                    same_point_count += 1
                else:
                    current_slope = slope(point1, point2)
                    slopes[current_slope] += 1
                    current_max = max(current_max, slopes[current_slope])

        # update the overall maximum count of points on a line
        max_points = max(max_points, current_max + same_point_count + 1)

    return max_points

points = [(1,1), (2,2), (3,3)]
print(maxPoints(points))

