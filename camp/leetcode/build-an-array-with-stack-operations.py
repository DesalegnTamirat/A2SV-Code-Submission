class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        i = 0
        number = 1
        while i < len(target):
            if target[i] == number:
                operations.append("Push")
                i += 1
            else:
                operations.extend(["Push", "Pop"])
            number += 1
        
        return operations
        
            