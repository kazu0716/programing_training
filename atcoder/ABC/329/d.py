N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = [0] * N
person, n = pow(10, 9), 0
ans = []
for a in A:
    cnt[a-1] += 1
    if cnt[a-1] > n:
        person, n = a, cnt[a-1]
    elif cnt[a-1] == n:
        person = min(person, a)
    ans.append(person)
print(*ans, sep='\n')
