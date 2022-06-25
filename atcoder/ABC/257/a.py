N, X = map(int, input().split())
ans = ""
for i in range(26):
    ans += chr(65+i) * N
print(ans[X-1])
