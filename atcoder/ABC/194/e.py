from collections import defaultdict, deque
from sys import exit

N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = defaultdict(int)
deq = deque([])

for i in range(M):
    cnt[A[i]] += 1
    deq.append(A[i])

ans = 0
while ans in cnt:
    ans += 1
if ans == 0:
    print(ans)
    exit()

for i in range(M, N):
    a, p = A[i], deq.popleft()
    deq.append(a)
    cnt[p] -= 1
    cnt[a] += 1
    if p < ans and cnt[p] == 0:
        ans = p

print(ans)
