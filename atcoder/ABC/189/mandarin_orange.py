N = int(input())
A = list(map(int, input().split()))

ans = 0
B = A[:]
B.sort()
st = set(B)

for x in st:
    s, t = 0, 0
    for a in A:
        if a >= x:
            t += x
            s = max(s, t)
        else:
            t = 0
    ans = max(ans, s)

print(ans)
