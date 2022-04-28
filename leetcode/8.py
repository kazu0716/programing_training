from urllib.parse import SplitResult


class Solution:
    def myAtoi(self, s: str) -> int:
        digits = ""
        for ss in s:
            if ss.isdecimal() or ((ss == "+" or ss == "-") and digits == ""):
                digits += ss
            elif ss == " " and digits == "":
                continue
            else:
                break
        if digits == "" or digits == "+" or digits == "-":
            return 0
        num = int(digits)
        if num > pow(2, 31) - 1:
            return pow(2, 31) - 1
        if num < -pow(2, 31):
            return -pow(2, 31)
        return num


if __name__ == "__main__":
    sol = Solution()
    s = "   123"
    print(sol.myAtoi(s))
