from collections import Counter

N = int(input())
candidates = []

for _ in range(N):
    S = input()
    candidates.append(S)

cnt = Counter(candidates)
ans = sorted(cnt.items(), key=lambda x: x[1])
print(ans[-1][0])
