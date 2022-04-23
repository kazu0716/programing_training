from collections import defaultdict

N, K = map(int, input().split())
counter = []
for _ in range(N):
    cnt = defaultdict(bool)
    S = input()
    for s in S:
        cnt[s] = True
    counter.append(cnt)
ans = 0
for i in range(2**N):
    dic = defaultdict(int)
    for idx, bit in enumerate(list(bin(i)[2:].rjust(N, "0"))):
        if bit == "0":
            continue
        for j in range(97, 123):
            if counter[idx][chr(j)]:
                dic[chr(j)] += 1
    count = 0
    for k in dic:
        if dic[k] == K:
            count += 1
    ans = max(ans, count)
print(ans)
