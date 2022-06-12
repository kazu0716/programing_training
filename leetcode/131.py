from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def traverse(string: str, palindromes: str) -> None:
            nonlocal ans
            if not string:
                ans.append(palindromes[1:].split(","))
                return
            for i in range(len(string)):
                if string[:i+1] == string[:i+1][::-1]:
                    traverse(string[i+1:], f"{palindromes},{string[:i+1]}")

        traverse(s, "")
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "aab"
    print(sol.partition(s))
