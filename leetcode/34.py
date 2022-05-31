from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.bisect("left", nums, target), self.bisect("right", nums, target)
        if left == right == -1:
            return [-1, -1]
        return [left, right]

    def bisect(self, type: str, nums: List[int], target: int) -> int:
        index, low, high = -1, 0, len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                index = mid
                if type == "left":
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index


if __name__ == "__main__":
    sol = Solution()
    nums, target = [5, 7, 7, 8, 8, 10], 8
    print(sol.searchRange(nums, target))
