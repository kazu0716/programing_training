class Solution:
    def solve1(self, s: str) -> str:
        """
        Simple solution

        Time complexity: O(N)
        Memory Space: O(N)
        """
        ret, cur, cnt = [], "", 0
        for ss in s:
            if cur != ss:
                if cnt > 0:
                    ret.append(cur + str(cnt))
                cur, cnt = ss, 1
            else:
                cnt += 1
        ret.append(cur + str(cnt))
        return "".join(ret)


if __name__ == "__main__":
    """
    String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
    For example, the string aabcccccaaa would become a2b1c5a3.
    If the "compressed "string would not become smaller than the original string, your method should return the original string.
    You can assume the string has only uppercase and lowercase letters (a - z)
    """
    S = input()
    sol = Solution()
    print(sol.solve1(S))
