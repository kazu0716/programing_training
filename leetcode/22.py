from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paren = []
        for i in range(pow(2, 2*n)):
            cnt, p = 0, ""
            for j in range(2*n):
                if (i >> j) & 1:
                    cnt += 1
                    p += "("
                else:
                    cnt -= 1
                    p += ")"
                if cnt < 0:
                    break
            if cnt == 0:
                paren.append(p)
        return paren


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))
