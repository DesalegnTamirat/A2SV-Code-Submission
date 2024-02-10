class Solution:
    def interpret(self, command: str) -> str:
        goal = []
        index = 0
        n = len(command)
        while index < n:
            if command[index] == "G":
                goal.append("G")
            elif command[index] + command[index + 1] == "()":
                goal.append("o")
                index += 1
            else:
                goal.append("al")
                index += 3
            index += 1
        return "".join(goal)