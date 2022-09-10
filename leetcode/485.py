from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, num_max = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                num_max = max(cnt, num_max)
                cnt = 0
        return max(cnt, num_max)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 0, 1, 1, 1]
    print(sol.findMaxConsecutiveOnes(nums))
