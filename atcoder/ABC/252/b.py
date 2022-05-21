from collections import defaultdict

N, K = map(int, input().split())
A, B = list(map(int, input().split())), set(map(int, input().split()))

cnt = defaultdict(set)
for i, a in enumerate(A):
    cnt[a].add(i+1)
if cnt[max(cnt)] & B:
    print("Yes")
else:
    print("No")
