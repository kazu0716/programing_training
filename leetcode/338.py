from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = [0] * (n+1)
        for i in range(n+1):
            if i == 0:
                cnt[0] = 0
            elif i == 1:
                cnt[1] = 1
            else:
                cnt[i] = cnt[i//2] if i % 2 == 0 else cnt[i-1] + 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    n = 10000
    print(sol.countBits(n))
