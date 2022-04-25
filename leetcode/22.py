from sys import setrecursionlimit
from typing import List

setrecursionlimit(pow(10, 6))


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(paren, cnt):
            nonlocal parens
            if len(paren) > 2*n or cnt < 0 or cnt - (2*n - len(paren)) > 0:
                return
            if len(paren) == 2*n and cnt == 0:
                parens.append(paren)
                return
            for nxt in ("(", ")"):
                dfs(paren + nxt, cnt + 1 if nxt == "(" else cnt - 1)
        parens = []
        dfs("", 0)
        return parens


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))
