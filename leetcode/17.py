from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_str, ret = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], []

        def dfs(numbers, strings):
            nonlocal ret
            if not numbers:
                if strings:
                    ret.append(strings)
                return
            for s in digits_str[int(numbers[0])-2]:
                dfs(numbers[1:], strings + s)

        dfs(digits, "")
        return ret


if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    print(sol.letterCombinations(digits))
