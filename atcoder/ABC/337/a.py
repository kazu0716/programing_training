N = int(input())
t, k = 0, 0
for _ in range(N):
    X, Y = map(int, input().split())
    t += X
    k += Y
if t == k:
    print("Draw")
elif t > k:
    print("Takahashi")
else:
    print("Aoki")
