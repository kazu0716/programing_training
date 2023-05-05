X, Y, Z, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)
ans = []
for i, a in enumerate(A):
    if i + 1 > K:
        break
    for j, b in enumerate(B):
        if (i + 1) * (j + 1) > K:
            break
        for k, c in enumerate(C):
            if (i + 1) * (j + 1) * (k + 1) > K:
                break
            ans.append(a + b + c)
print(*sorted(ans, reverse=True)[:K], sep="\n")
