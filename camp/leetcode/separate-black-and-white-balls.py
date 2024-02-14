class Solution:
    def minimumSteps(self, s: str) -> int:
        colors = list(s)
        write = 0
        read = 0
        swaps = 0
        while read < len(colors):
            if colors[read] == "0":
                colors[read], colors[write] = colors[write], colors[read]
                swaps += read - write
                write += 1
            read += 1

        return swaps