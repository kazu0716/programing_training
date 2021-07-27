N, M = map(int, input().split())
ans = [-1] * N
flag = True

for _ in range(M):
    s, c = map(int, input().split())
    s -= 1
    if (ans[s] != -1 and ans[s] != c) or (s == 0 and c == 0 and N > 1):
        flag = False
        break
    ans[s] = c

if flag:
    result = 0
    for i in range(N):
        n = ans[i]
        if (n == -1 and i != 0) or (n == -1 and i == 0 and N == 1):
            n = 0
        elif n == -1 and i == 0 and N != 1:
            n = 1
        result += n * pow(10, N-(i+1))
    print(result)
else:
    print(-1)
