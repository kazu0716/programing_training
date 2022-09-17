from sys import setrecursionlimit

setrecursionlimit(pow(10, 9))


def dfs(pos: int, bit: str) -> None:
    if pos == len(n_bit):
        ans.append(int(bit, 2))
        return
    if n_bit[pos] == "1":
        dfs(pos+1, bit + "1")
    dfs(pos+1, bit + "0")


N = int(input())
n_bit, ans = bin(N)[2:], []
dfs(0, "")
ans.sort()
print(*ans, sep="\n")
