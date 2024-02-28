class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        answer = []
        # push everything till we find closed
        for let in s:
            # if we find close pop till we find open
            # and append the decoded
            if let == "]":
                decode = []
                while stack[-1] != "[":
                    decode.append(stack.pop())
                stack.pop()
                digits = []
                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())
                num = int("".join(reversed(digits)))
                stack.extend(reversed(num * decode))
            else:
                stack.append(let)

        return "".join(stack)
        