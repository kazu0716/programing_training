N = int(input())
p_max = 0
ans = 0
for _ in range(N):
    p = int(input())
    p_max = max(p_max, p)
    ans += p
print(ans - p_max // 2)
