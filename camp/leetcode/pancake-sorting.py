class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)

        for i in range(n - 1, 0, -1):
            maximum = max(arr[:i + 1])
            start = 0
            end = arr.index(maximum)
            if end == i:
                continue
            ans.append(end + 1)
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

            start = 0
            end = i
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            
            ans.append(i + 1)

        return ans