from collections import Counter
from sys import setrecursionlimit

from pypyjit import set_param

setrecursionlimit(pow(10, 9))
set_param("max_unroll_recursion=-1")


def dfs(cur):
    for nxt in "357":
        num = cur + nxt
        if len(num) < 3:
            dfs(num)
        if len(num) > length:
            return
        if int(num) > N:
            continue
        if "".join(sorted(Counter(num).keys())) == "357":
            if num in ans:
                continue
            ans.add(num)
        dfs(num)


N = int(input())
length = len(str(N))
ans = set()
dfs("")
print(len(ans))
