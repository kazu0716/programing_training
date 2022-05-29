class Solution:
    def longestPalindrome(self, s: str) -> str:
        length, ans = 0, ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                txt = s[i:j+1]
                if txt == txt[::-1] and len(txt) > length:
                    length, ans = len(txt), txt
            if len(s[i:]) == length:
                break
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "aacabdkacaa"
    print(sol.longestPalindrome(s))
