T = int(input())
N = int(input())
clerks = [0] * (T + 1)
for _ in range(N):
    L, R = map(int, input().split())
    clerks[L] += 1
    clerks[R] -= 1
for i in range(T):
    clerks[i + 1] += clerks[i]
print(*clerks[:-1], sep="\n")
