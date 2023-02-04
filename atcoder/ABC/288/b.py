N, K = map(int, input().split())
s = []
for _ in range(N):
    s.append(input())
print(*sorted(s[:K]), sep="\n")
