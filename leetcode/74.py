from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        low, high = 0, len(matrix)*(len(matrix[0]))-1
        while low <= high:
            mid = (low+high)//2
            y, x = divmod(mid, len(matrix[0]))
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(sol.searchMatrix(matrix, target))
