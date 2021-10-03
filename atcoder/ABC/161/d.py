from itertools import chain

K = int(input())

dp = [[] for _ in range(10)]
dp[0] = list(range(1, 10))

for i in range(1, 10):
    for j in dp[i-1]:
        high = j * 10
        for low in range(j % 10 - 1, j % 10 + 2):
            if low < 0 or low > 9:
                continue
            dp[i].append(high+low)

dp = list(chain.from_iterable(dp))
print(dp[K-1])
