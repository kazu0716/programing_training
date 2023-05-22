N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
diff, ans = pow(10, 9), 0
for i, h in enumerate(H):
    t = T - h * 0.006
    if abs(A - t) < diff:
        diff = abs(A - t)
        ans = i + 1
print(ans)
