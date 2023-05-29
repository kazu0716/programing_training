from collections import defaultdict

n = int(input())
v = list(map(int, input().split()))
cnt_odd = defaultdict(int)
cnt_even = defaultdict(int)
for i, vv in enumerate(v):
    if i % 2 == 0:
        cnt_even[vv] += 1
    else:
        cnt_odd[vv] += 1
sorted_cnt_odd = sorted(cnt_odd.items(), key=lambda x: x[1])
sorted_cnt_even = sorted(cnt_even.items(), key=lambda x: x[1])
if len(sorted_cnt_odd) == len(sorted_cnt_even) == 1 and sorted_cnt_odd[-1][0] == sorted_cnt_even[-1][0]:
    print(n // 2)
    exit()
if sorted_cnt_odd[-1][0] != sorted_cnt_even[-1][0]:
    print(n - sorted_cnt_odd[-1][1] - sorted_cnt_even[-1][1])
    exit()
cnt1 = sorted_cnt_odd[-1][1] + (sorted_cnt_even[-2][1] if len(sorted_cnt_even) >= 2 else 0)
cnt2 = sorted_cnt_even[-1][1] + (sorted_cnt_odd[-2][1] if len(sorted_cnt_odd) >= 2 else 0)
print(n - max(cnt1, cnt2))
