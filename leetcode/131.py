from sys import setrecursionlimit
from typing import List

setrecursionlimit(pow(10, 6))


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Time complexity : O(n^2)
        Space complexity : O(n^2)

        ref: https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution
        """
        ans = []

        def traverse(string: str, palindromes: List[str]) -> None:
            nonlocal ans
            if not string:
                ans.append(palindromes)
                return
            for i in range(len(string)):
                if string[:i+1] == string[:i+1][::-1]:
                    traverse(string[i+1:], palindromes + [string[:i+1]])

        traverse(s, [])
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "aab"
    print(sol.partition(s))
