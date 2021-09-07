from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        ans, cnt = 0, 1
        dic = {}
        for i in range(len(s)):
            ch = s[i]
            if ch in dic:
                start = max(start, dic[ch] + 1)
            dic[ch] = i
            cnt = i - start + 1
            ans = max(cnt, ans)
        return ans
