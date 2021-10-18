N = int(input())

line = []
T = 0.0

for _ in range(N):
    A, B = map(int, input().split())
    line.append((A, B))
    T += A/B

T /= 2
ans = 0.0

for i in range(N):
    A, B = line[i]
    if T >= A/B:
        ans += A
        T -= A/B
    else:
        ans += B*T
        break

print(ans)
