class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        for fir_start, fir_end in firstList:
            for sec_start, sec_end in secondList:
                if fir_start <= sec_start <= fir_end or fir_start <= sec_end <= fir_end or sec_start <= fir_start <= sec_end or sec_start <= fir_end <= sec_end:
                    ans.append([max(fir_start, sec_start), min(fir_end, sec_end)])
        
        return ans
                