from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i+1-len(word):i+1] and (dp[i-len(word)] or i-len(word) == -1):
                    dp[i] = True
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s, wordDict))
