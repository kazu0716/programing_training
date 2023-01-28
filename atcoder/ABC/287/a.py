N = int(input())
cnt = 0
for _ in range(N):
    S = input()
    if S == "For":
        cnt += 1
print("Yes" if cnt > N // 2 else "No")
