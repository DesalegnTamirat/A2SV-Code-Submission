class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        right = 0
        maximum = 0
        temp = k
        n = len(answerKey)
        while left < n and right < n:
            while right < n and (k > 0 or answerKey[right] == "T"):
                if answerKey[right] == "F":
                    k -= 1
                right += 1
            maximum = max(maximum, right - left)
            if answerKey[left] == "F":
                k += 1
            left += 1
        
        false_to_true = max(maximum, right - left)

        k = temp
        left = 0
        right = 0
        maximum = 0
        while left < n and right < n:
            while right < n and (k > 0 or answerKey[right] == "F"):
                if answerKey[right] == "T":
                    k -= 1
                right += 1
            maximum = max(maximum, right - left)
            if answerKey[left] == "T":
                k += 1
            left += 1

        true_to_false = max(right - left, maximum)

        return max(true_to_false, false_to_true)
