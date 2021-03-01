N = int(input())
taka = []
ao, ans = 0, 0

for _ in range(N):
    a, b = map(int, input().split())
    taka.append(2*a + b)
    ao += a

taka.sort()

while ao >= 0:
    ao -= taka.pop()
    ans += 1

print(ans)
