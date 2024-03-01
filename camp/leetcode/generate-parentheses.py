class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        par = []
        def backtrack(balance):
            if len(par) == 2 * n:
                if balance == 0:
                    ans.append("".join(par))
                return
            
            
            par.append("(")
            backtrack(balance + 1)
            par.pop()
            if balance > 0:
                par.append(")")
                backtrack(balance - 1)
                par.pop()
            
        backtrack(0)
        return ans




            