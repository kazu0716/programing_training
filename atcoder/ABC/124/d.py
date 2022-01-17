from collections import deque

N, K = map(int, input().split())
S = input()

cnt0, cnt1 = 0, 0
run_len = []
for s in S:
    if s == "0":
        cnt0 += 1
        if cnt1 > 0:
            run_len.append(("1", cnt1))
            cnt1 = 0
    else:
        cnt1 += 1
        if cnt0 > 0:
            run_len.append(("0", cnt0))
            cnt0 = 0

if cnt1 > 0:
    run_len.append(("1", cnt1))
    cnt1 = 0
else:
    run_len.append(("0", cnt0))
    cnt0 = 0

l, queue = 0, deque([])
cnt, ans = 0, 0
for r in range(len(run_len)):
    bit, c = run_len[r]
    if bit == "0" and l >= K:
        while queue:
            b, cc = queue.popleft()
            cnt -= cc
            if b == "0":
                l -= 1
                break
    queue.append((bit, c))
    cnt += c
    if bit == "0":
        l += 1
    ans = max(ans, cnt)

print(ans)
