class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans = []
        ones = 0
        # counting how many ones are there to the right
        for num in nums:
            if num == 1:
                ones += 1

        highest_score = ones
        ans = [0]
        zeros = 0
        for i, num in enumerate(nums):
            # enumerating and decreasing one and increasing zero
            if num == 0:
                zeros += 1
            else:
                ones -= 1
            
            #calculating the score and comparing with the highest so far
            score = zeros + ones
            if score == highest_score:
                ans.append(i + 1)
            elif score > highest_score:
                ans = [i + 1]
                highest_score = score

        return ans
            
        
        
