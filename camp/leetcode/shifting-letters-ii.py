class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_sum = [0] * n
        for start, end, direction in shifts:
            if direction == 0:
                prefix_sum[start] += -1
                if end < (n - 1):
                    prefix_sum[end + 1] += 1
            else:
                prefix_sum[start] += 1
                if end < (n - 1):
                    prefix_sum[end + 1] += -1

        running_sum = []
        accumulator = 0
        for ssum in prefix_sum:
            accumulator += ssum
            running_sum.append(accumulator)
        
        ans = ""
        for i in range(n):
            ascii_code = (ord(s[i]) + running_sum[i] - ord("a")) % 26
            ans += chr(ascii_code + 97)
            
        return ans



        
