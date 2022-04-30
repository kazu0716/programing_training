class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        pos1, pos2 = 1, 2
        for _ in range(3, n+1):
            pos1, pos2 = pos2, pos1 + pos2
        return pos2


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.climbStairs(n))
