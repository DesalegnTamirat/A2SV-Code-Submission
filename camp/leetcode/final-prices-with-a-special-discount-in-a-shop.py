class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(prices)
        for i in range(len(answer) - 1, -1, -1):
            price = prices[i]
            while stack and price < stack[-1]:
                stack.pop()
            
            if not stack:
                answer[i] = price
            else:
                answer[i] = price - stack[-1]
            
            stack.append(price)

        return answer
        