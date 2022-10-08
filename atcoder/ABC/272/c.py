N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
max_odd1, max_odd2, max_even1, max_even2 = -1, -1, -1, -1
for a in A:
    if a % 2 == 0:
        if max_even1 == -1:
            max_even1 = a
        elif max_even2 == -1:
            max_even2 = a
    else:
        if max_odd1 == -1:
            max_odd1 = a
        elif max_odd2 == -1:
            max_odd2 = a
if (max_even1 == -1 or max_even2 == -1) and (max_odd1 == -1 or max_odd2 == -1):
    print(-1)
else:
    print(max(max_even1+max_even2, max_odd1+max_odd2))
