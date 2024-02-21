class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        # sort guards and walls to know the location easily
        row_col = lambda cell: (cell[0], cell[1])
        guards.sort(key=row_col)
        walls.sort(key=row_col)

        # traverse and locate walls and guards
        i = j = 0
        for row in range(m):
            for col in range(n):
                if i == len(guards) and j == len(walls):
                    break
                if i < len(guards) and guards[i] == [row, col]:
                    grid[row][col] = "G"
                    i += 1
                elif j < len(walls) and walls[j] == [row, col]:
                    grid[row][col] = "W"
                    j += 1
        
        # by traversing all four direction let see guarded and unguarded
        # traversing we first assume it is unguarded till we hit a guard
        # left traversing
        for row in range(m):
            unguarded = True
            for col in range(n):
                if grid[row][col] == "G":
                    unguarded = False
                elif grid[row][col] == "W":
                    unguarded = True
                elif unguarded:
                    grid[row][col] = True
                else:
                    grid[row][col] = False

        # right traversing
        for row in range(m):
            unguarded = True
            for col in range(n - 1, -1, -1):
                if grid[row][col] == "G":
                    unguarded = False
                elif grid[row][col] == "W":
                    unguarded = True
                elif unguarded:
                    grid[row][col] = grid[row][col] and True
                else:
                    grid[row][col] = False

        #  traversing down
        for col in range(n):
            unguarded = True
            for row in range(m):
                if grid[row][col] == "G":
                    unguarded = False
                elif grid[row][col] == "W":
                    unguarded = True
                elif unguarded:
                    grid[row][col] = grid[row][col] and True
                else:
                    grid[row][col] = False
        
        # traversing up
        for col in range(n):
            unguarded = True
            for row in range(m - 1, -1, -1):
                if grid[row][col] == "G":
                    unguarded = False
                elif grid[row][col] == "W":
                    unguarded = True
                elif unguarded:
                    grid[row][col] = grid[row][col] and True
                else:
                    grid[row][col] = False

        # finally lets count the call that are True for all which means unguarded in all direction
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "G":
                    pass
                elif grid[row][col] == "W":
                    pass
                elif grid[row][col]:
                    count += 1

        return count


