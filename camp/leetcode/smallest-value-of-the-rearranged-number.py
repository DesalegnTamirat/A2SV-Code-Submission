class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num
        elif num > 0:
            pos = True
        else:
            pos = False
        
        nums = list(map(int, str(abs(num))))
        nums.sort()
        if pos:
            i = 0
            while nums[i] == 0:
                i += 1
            nums[i], nums[0] = nums[0], nums[i]
            return int("".join(list(map(str, nums))))
        else:
            return -1 * int("".join(list(map(str, nums))[::-1]))
