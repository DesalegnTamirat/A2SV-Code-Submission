class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            start = 0
            end = len(image) - 1
            while start <= end:
                image[row][start] = int(not image[row][start])
                if start != end:
                    image[row][end] = int(not image[row][end])
                    image[row][start], image[row][end] = image[row][end], image[row][start]
                start += 1
                end -= 1
            
        return image