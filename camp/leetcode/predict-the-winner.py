class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        left = 0
        right = n - 1
        turn = "first"
        first_player = self.choose(nums, left, right, turn)
        second_player = sum(nums) - first_player
        return first_player >= second_player

    def choose(self, nums, left, right, turn):
        if left > right:
            return 0
        
        # if first turn choose the maximum
        if turn == "first":
            one_option = self.choose(nums, left + 1, right, "second")
            other_option = self.choose(nums, left, right - 1, "second")
            return max(nums[left] + one_option, nums[right] + other_option)
        
        # if second turn make it minimum
        one_option = self.choose(nums, left + 1, right, "first")
        other_option = self.choose(nums, left, right - 1, "first")
        return min(one_option, other_option)
        
