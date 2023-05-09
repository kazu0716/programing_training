from collections import deque

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
targets = {"A": A, "B": B, "C": C}
queue = deque([(0, {"A": 0, "B": 0, "C": 0, "D": 0}, {"A": 0, "B": 0, "C": 0, "D": 0})])
ans = pow(10, 6)
while queue:
    i, cur_length, cur_cnt = queue.popleft()
    for key in "ABCD":
        nxt_length, nxt_cnt = cur_length.copy(), cur_cnt.copy()
        nxt_length[key] += L[i]
        nxt_cnt[key] += 1
        if i < N - 1:
            queue.append((i + 1, nxt_length, nxt_cnt))
            continue
        is_zero, mp = False, 0
        for k in "ABC":
            if nxt_cnt[k] == 0:
                is_zero = True
            mp += 10 * (nxt_cnt[k] - 1 if nxt_cnt[k] > 1 else 0) + abs(targets[k] - nxt_length[k])
        if not is_zero and ans > mp:
            ans = mp
print(ans)
