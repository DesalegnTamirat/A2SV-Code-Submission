class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        total_moves = 0
        while target > 1:
            if maxDoubles > 0:
                # if it is even only use double
                if target % 2 == 0:
                    total_moves += 1
                else:
                    total_moves += 2
                # if odd doubling and adding
                target //= 2
                maxDoubles -= 1
            else:
                total_moves += target - 1
                target = 1
        
        return total_moves




        