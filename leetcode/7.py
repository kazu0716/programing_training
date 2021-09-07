class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
        rev = list(str(x))[::-1]
        if flag:
            rev.pop()
            ans = -int("".join(rev))
        else:
            ans = int("".join(rev))
        if ans > pow(2, 31) - 1 or ans < - pow(2, 31):
            ans = 0
        return ans
