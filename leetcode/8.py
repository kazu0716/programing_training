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
        num, ma, mi = int(digits), pow(2, 31) - 1, -pow(2, 31)
        if num > ma:
            return ma
        if num < mi:
            return mi
        return num


if __name__ == "__main__":
    sol = Solution()
    s = "   123"
    print(sol.myAtoi(s))
