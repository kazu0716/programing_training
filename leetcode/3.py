class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r, sub = 0, set()
        max_length = 0
        for l in range(len(s)):
            while r < len(s) and s[r] not in sub:
                sub.add(s[r])
                r += 1
            max_length = max(max_length, r - l)
            sub.remove(s[l])
        return max_length


if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))
