class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Time complexity : O(N ^ 2)
        Space complexity : O(1)
        """
        cnt = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                strings = s[i] if i == j else s[i:j+1]
                if strings == strings[::-1]:
                    cnt += 1
        return cnt

    def countSubstrings2(self, s: str) -> int:
        """
        Time complexity : O(N)
        Space complexity : O(1)
        """
        cnt, s = len(s), "".join([s if i == 0 else "#"+s for i, s in enumerate(s)])
        for i in range(len(s)):
            d = 1
            while 0 <= i-d and i+d <= len(s)-1 and s[i-d] == s[i+d]:
                if (s[i] == "#" or d > 1) and s[i-d] == s[i+d] != "#":
                    cnt += 1
                d += 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    s = "aaaaa"
    print(sol.countSubstrings2(s))
