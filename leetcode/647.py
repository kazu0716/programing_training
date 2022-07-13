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


if __name__ == "__main__":
    sol = Solution()
    s = "aaa"
    print(sol.countSubstrings(s))
