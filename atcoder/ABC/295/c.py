from collections import Counter

N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
ans = 0
for key in counter:
    ans += counter[key] // 2
print(ans)
