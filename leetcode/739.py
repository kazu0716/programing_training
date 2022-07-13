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

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        """
        Time complexity : O(N)
        Space complexity : O(1)
        """
        hottest, answer = 0, [0] * len(temperatures)
        # NOTE: search tmp from back
        for i in range(len(temperatures) - 1, -1, -1):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
                continue
            days = 1
            while temperatures[i + days] <= temperatures[i]:
                days += answer[i + days]
            answer[i] = days
        return answer


if __name__ == "__main__":
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures2(temperatures))
