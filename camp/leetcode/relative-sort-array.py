class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = {value: index for index, value in enumerate(arr2)}
        for num in arr1:
            if num not in arr2_set:
                arr2_set[num] = float("inf")
                
                
        return sorted(arr1, key=lambda value: (arr2_set[value], value))