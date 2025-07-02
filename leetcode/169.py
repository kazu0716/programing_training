# ref: https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer–Moore majority vote algorithm
        ref: https://qiita.com/tatmius/items/37707bce1ef079616c93

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        candidate, cnt = 0 ,0
        for num in nums:
            if cnt != 0:
                cnt += 1 if candidate == num else -1
                continue
            candidate = num
            cnt += 1
        return candidate
                


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 3, 4, 2, 4, 2, 4, 4]
    print(sol.majorityElement(nums))
