from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        ans, stack = [0]*len(temperatures), []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, j = stack.pop()
                ans[j] = i-j
            stack.append((t, i))
        return ans


if __name__ == "__main__":
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(temperatures))
