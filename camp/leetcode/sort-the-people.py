class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_heights = []
        for i in range(len(names)):
            names_heights.append([names[i], heights[i]])

        sorted_names_heights = sorted(names_heights, key = lambda name_height: name_height[1], reverse = True)

        return [name_height[0] for name_height in sorted_names_heights]