from sys import setrecursionlimit

from pypyjit import set_param

setrecursionlimit(pow(10, 9))
set_param("max_unroll_recursion=-1")


def dfs(pos, cur):
    for bit in "10" if S[pos] == "?" else S[pos]:
        nxt = cur + (pow(2, len(S) - 1 - pos) if bit == "1" else 0)
        if nxt > N:
            continue
        if pos + 1 >= len(S):
            print(nxt)
            exit()
        dfs(pos + 1, nxt)


S = input()
N = int(input())
dfs(0, 0)
print(-1)
