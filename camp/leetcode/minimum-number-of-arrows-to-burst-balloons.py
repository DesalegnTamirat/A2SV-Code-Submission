class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        n = len(points)
        count = 0
        i = 0
        while i < n:
            j = i + 1
            fir_start, fir_end = points[i]
            count += 1
            while j < n:
                sec_start, sec_end = points[j]
                if fir_start <= sec_start <= fir_end or fir_start <= sec_end <= fir_end or sec_start <= fir_start <= sec_end or sec_start <= fir_end <= sec_end:
                    fir_start, fir_end = [max(fir_start, sec_start), min(fir_end, sec_end)]
                else:
                    break
                j += 1
                
            i = j

        return count