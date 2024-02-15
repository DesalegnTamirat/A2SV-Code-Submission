class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda point: point[0])
        maximum_gap = 0
        prev_point = points[0][0]
        for point, _ in points[1:]:
            maximum_gap = max(maximum_gap, point - prev_point)
            prev_point = point
        
        return maximum_gap