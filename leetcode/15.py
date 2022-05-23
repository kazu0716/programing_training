from collections import Counter
from typing import List, Set, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> Set[Tuple[int]]:
        cnt, three_sum = Counter(nums), set()
        nums = sorted(cnt.keys())
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            for j in range(i, len(nums)):
                cnt[nums[i]] -= 1
                cnt[nums[j]] -= 1
                num_k = -(nums[i]+nums[j])
                if nums[j] > num_k:
                    cnt[nums[i]] += 1
                    cnt[nums[j]] += 1
                    break
                if cnt[nums[i]] >= 0 and cnt[nums[j]] >= 0 and cnt[num_k] > 0:
                    three_sum.add((nums[i], nums[j], num_k))
                cnt[nums[i]] += 1
                cnt[nums[j]] += 1
        return three_sum


if __name__ == "__main__":
    sol = Solution()
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    print(sol.threeSum(nums))
