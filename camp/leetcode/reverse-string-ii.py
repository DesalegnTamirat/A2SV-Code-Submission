class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        letters = list(s)
        for i in range(0, n, 2 * k):
            left = n - i
            if left < k:
                # reverse all
                l = i
                r = n - 1
                while l < r:
                    letters[l], letters[r] = letters[r], letters[l]
                    l += 1
                    r -= 1
                break
            elif left < 2 * k:
                l = i
                r = i + k - 1
                while l < r:
                    letters[l], letters[r] = letters[r], letters[l]
                    l += 1
                    r -= 1
                break
            else:
                l = i
                r = i + k - 1
                while l < r:
                    letters[l], letters[r] = letters[r], letters[l]
                    l += 1
                    r -= 1
        
        return "".join(letters)

                