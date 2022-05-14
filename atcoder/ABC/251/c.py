from collections import defaultdict

N = int(input())
result = defaultdict(tuple)
for i in range(N):
    S, T = input().split()
    if S not in result:
        result[S] = (int(T), i)
ans = [0, 0]
for k in result:
    if ans[0] < result[k][0] or (ans[0] == result[k][0] and ans[1] > result[k][1]):
        ans = result[k]
print(ans[1]+1)
