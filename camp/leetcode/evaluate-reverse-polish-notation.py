class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(eval(str(num1) + str(token) + str(num2))))
            else:
                stack.append(token)

        return int(stack[0])