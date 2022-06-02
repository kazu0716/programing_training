from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        cur, nxt, step, i = -1, 0, 0, 0
        while nxt < len(nums)-1:
            if cur < i:
                step += 1
                cur = nxt
            nxt = max(nxt, nums[i]+i)
            i += 1
        return step


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1, 1, 4]
    print(sol.jump(nums))
