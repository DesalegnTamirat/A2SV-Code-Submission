class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = []
        n = len(nums)
        nums.sort()
        first = 0
        while first < n:
            # ignoring duplicates
            while 0 < first < n and nums[first] == nums[first - 1]:
                first += 1
            if first == n:
                break
            
            second = first + 1
            while second < n:
                # ignoring duplicates
                while first + 1 < second < n and nums[second] == nums[second - 1]:
                    second += 1
                if second == n:
                    break

                # the sum we are looking to reach target
                sum_target = target - nums[first] - nums[second]
                left = second + 1
                right = n - 1
                # using two pointer to decide which way to go
                # increase left if we want to increase sum
                # else decrease right to decrease sum
                while left < right:
                    two_sum = nums[left] + nums[right]
                    if two_sum == sum_target:
                        quadruplets.append([nums[first], nums[second], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # avoiding duplicates for the left pointer
                        while left < n and nums[left] == nums[left - 1]:
                            left += 1

                        # avoiding duplicates for the right pointer
                        while n - 1 < right >= 0 and nums[right] == nums[right + 1]:
                            right += 1
                    elif two_sum < sum_target:
                        left += 1
                    else:
                        right -= 1
                
                second += 1
            
            first += 1

        return quadruplets
                