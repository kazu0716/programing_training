T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = map(int, input().split())
    cnt = 0
    for a in A:
        if a % 2 == 1:
            cnt += 1
    ans.append(cnt)
print(*ans, sep="\n")
