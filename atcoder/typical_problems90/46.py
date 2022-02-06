N = int(input())
A, B, C = [0]*46, [0]*46, [0]*46
for l in (A, B, C):
    for i in map(int, input().split()):
        l[i % 46] += 1
ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k) % 46 == 0:
                ans += A[i]*B[j]*C[k]
print(ans)
