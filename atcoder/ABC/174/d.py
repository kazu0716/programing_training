N = int(input())
C = input()

a, b = 0, 0
for i in range(N):
    if C[i] != "W":
        b += 1

s = ["W"] * N
ans = max(a, b)

for i in range(1, N+1):
    s[i-1] = "R"
    if s[i-1] == C[i-1]:
        b -= 1
    else:
        a += 1
    ans = min(ans, max(a, b))

print(ans)
