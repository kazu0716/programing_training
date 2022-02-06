N = int(input())
coin = sorted(list(map(int, input().split())))
A, B, C = coin[-1], coin[-2], coin[-3]

ans = pow(10, 9)
for i in range(N//A+1):
    for j in range((N-A*i)//B+1):
        k, r = divmod(N-A*i-B*j, C)
        if r == 0:
            ans = min(ans, i+j+k)
print(ans)
