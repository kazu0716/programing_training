from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    s = input()
    print(sol.firstUniqChar(s))
