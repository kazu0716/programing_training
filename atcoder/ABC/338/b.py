from collections import defaultdict

S = input()
cnt = defaultdict(int)
for s in S:
    cnt[s] += 1
print(sorted([(-v, k) for k, v in cnt.items()])[0][1])
