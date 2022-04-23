from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[nums[i]] for i in range(len(nums))]
        for _ in range(len(nums) - 1):
            tmp = []
            while perms:
                perm1 = perms.pop()
                for num in set(nums) ^ set(perm1):
                    perm2 = perm1.copy()
                    perm2.append(num)
                    tmp.append(perm2)
            perms = tmp
        return perms


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permute(nums))
