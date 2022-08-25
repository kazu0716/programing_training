from itertools import accumulate

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))
s = [0] + list(accumulate(A))
s_set = set(s)
for x in range(N):
    if s[x] + P in s_set and s[x] + P + Q in s_set and s[x] + P + Q + R in s_set:
        print("Yes")
        exit()
print("No")
