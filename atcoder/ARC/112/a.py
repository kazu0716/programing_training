T = int(input())
ans = []
for _ in range(T):
    L, R = map(int, input().split())
    ans.append((R-2*L+2)*(R-2*L+1)//2 if R-2*L+1 > 0 else 0)
print(*ans, sep="\n")
