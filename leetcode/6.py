class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        strings = [""] * numRows
        row, step = 0, -1
        for ss in s:
            strings[row] += ss
            if not(0 < row < numRows-1):
                step *= -1
            row += step
        return "".join(strings)


if __name__ == "__main__":
    sol = Solution()
    s = "AB"
    numRows = 1
    print(sol.convert(s, numRows))
