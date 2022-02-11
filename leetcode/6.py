class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = [[] for _ in range(numRows)]
        cur, add = 0, 1
        for ss in s:
            zigzag[cur].append(ss)
            if cur + add < 0:
                add = 1
            elif cur + add >= numRows:
                add = -1
            cur += add
        ret = []
        for i in range(numRows):
            ret += zigzag[i]
        return "".join(ret)
