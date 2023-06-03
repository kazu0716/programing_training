S = input()
K = int(input())
cnt = 0
for s in S:
    if s != "1":
        break
    cnt += 1
print(1 if cnt >= K else S[cnt])
