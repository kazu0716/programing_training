from collections import defaultdict
from typing import Dict, List


def dp_loop(_list: List[int], _range: range, dp: List[Dict[int, bool]]) -> None:
    for i, n in enumerate(_list):
        for j in _range:
            if j not in dp[i]:
                continue
            for nxt in (j - n, j + n):
                if _range[0] <= nxt <= _range[-1]:
                    dp[i+1][nxt] = True


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
x_list, y_list = [], []
for i in range(N):
    if i % 2 == 0 and i > 0:
        x_list.append(A[i])
    elif i % 2 == 1:
        y_list.append(A[i])
max_x, max_y = max(x_list) if x_list else X, max(y_list) if y_list else Y
x_range, y_range = range(-max_x * N, max_x * N + 1), range(-max_y * N, max_y * N + 1)
x_dp: List[Dict[int, bool]] = [defaultdict(bool) for _ in range(len(x_list) + 1)]
y_dp: List[Dict[int, bool]] = [defaultdict(bool) for _ in range(len(y_list) + 1)]
x_dp[0][A[0]], y_dp[0][0] = True, True
dp_loop(x_list, x_range, x_dp)
dp_loop(y_list, y_range, y_dp)
print("Yes" if x_dp[-1][X] and y_dp[-1][Y] else "No")
