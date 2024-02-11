class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        increasing = True
        for i in range(1, len(arr)):
            if i == 1 and arr[i] <= arr[i - 1]:
                return False
            if arr[i] == arr[i - 1]:
                return False
            elif arr[i] < arr[i - 1]:
                if increasing:
                    increasing = False
            elif arr[i] > arr[i - 1]:
                if not increasing:
                    return False
        
        return not increasing