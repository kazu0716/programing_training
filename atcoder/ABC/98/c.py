_ = int(input())
S = input()
cnt_sum = [{"W": 0, "E": 0}]
for s in S:
    last = cnt_sum[-1].copy()
    last[s] += 1
    cnt_sum.append(last)
ans = pow(10, 18)
for i, s in enumerate(S):
    i += 1
    ans = min(ans, cnt_sum[i - 1]["W"] + cnt_sum[-1]["E"] - cnt_sum[i]["E"])
print(ans)
