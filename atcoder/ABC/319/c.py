from itertools import permutations
from typing import List


def get_disappointed_list(h: int, w: int) -> List[tuple]:
    disappointed: List[tuple] = []
    # NOTE: horizontal
    for i in range(h):
        for p in permutations([i * w + j for j in range(w)]):
            if C[p[0]] == C[p[1]] != C[p[2]]:
                disappointed.append(p)
    # NOTE: vertical
    for j in range(w):
        for p in permutations([j + i * w for i in range(h)]):
            if C[p[0]] == C[p[1]] != C[p[2]]:
                disappointed.append(p)
    # NOTE: diagonal
    for angle in ((0, 4, 8), (2, 4, 6)):
        for p in permutations(angle):
            if C[p[0]] == C[p[1]] != C[p[2]]:
                disappointed.append(p)
    return disappointed


def is_disappointed(s: tuple, t_list: List[tuple]) -> bool:
    for t in t_list:
        # NOTE: Get not continuous substring length of t from s
        i = cnt = 0
        for ss in s:
            if i >= len(t):
                return True
            if ss == t[i]:
                cnt += 1
                i += 1
        if len(t) == cnt:
            return True
    return False


C = []
H = W = 3
for _ in range(H):
    C += input().split()
disappointed_list = get_disappointed_list(H, W)
ans = 0
for p in permutations(range(H * W)):
    if not is_disappointed(p, disappointed_list):
        ans += 1
print(ans / 362880)  # 9! = 362880
