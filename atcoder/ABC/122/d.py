from collections import defaultdict
from functools import reduce
from typing import Dict, List


def add_mod(x, y):
    return (x + y) % MOD


def contain_AGC(s: str) -> bool:
    for i in range(len(s)):
        s_list = list(s)
        if i > 0:
            s_list[i - 1], s_list[i] = s_list[i], s_list[i - 1]
        if "AGC" in "".join(s_list):
            return True
    return False


N = int(input())
MOD = pow(10, 9) + 7
dp: List[Dict[str, int]] = [defaultdict(int) for _ in range(N + 1)]
dp[0]["***"] = 1
for i in range(1, N + 1):
    for tail in dp[i - 1]:
        for c in "ACGT":
            if contain_AGC(tail + c):
                continue
            dp[i][tail[1:] + c] = (dp[i][tail[1:] + c] + dp[i - 1][tail]) % MOD
print(reduce(add_mod, dp[-1].values()))
