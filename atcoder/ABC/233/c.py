from itertools import product

N, X = map(int, input().split())
L = []
for _ in range(N):
    tmp = []
    for i, a in enumerate(list(map(int, input().split()))):
        if i == 0:
            continue
        tmp.append(a)
    L.append(tmp)

ans = 0
for p in product(*L):
    cnt = 1
    for pp in p:
        if cnt > X:
            break
        cnt *= pp
    if X != cnt:
        continue
    ans += 1

print(ans)
