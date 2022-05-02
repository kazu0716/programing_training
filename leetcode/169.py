from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, candidate = 0, None
        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += 1 if candidate == num else -1
        return candidate


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 3, 4, 2, 4, 2, 4, 4]
    print(sol.majorityElement(nums))
