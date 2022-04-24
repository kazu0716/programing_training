from sys import setrecursionlimit
from typing import List

setrecursionlimit(pow(10, 9))


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(path, idx, s):
            nonlocal pathes
            if s >= target:
                if s == target:
                    pathes.append([candidates[i] for i in path])
                return
            for nxt in range(idx, len(candidates)):
                dfs(path + [nxt], nxt, s + candidates[nxt])

        pathes = []
        dfs([], 0, 0)
        return pathes


if __name__ == "__main__":
    sol = Solution()
    candidates = [48, 22, 49, 24, 26, 47, 33, 40, 37, 39, 31, 46, 36, 43, 45, 34, 28, 20, 29, 25, 41, 32, 23]
    target = 69
    print(sol.combinationSum(candidates, target))
