from bisect import bisect_left, bisect_right

N = int(input())
S = input()
W = list(map(int, input().split()))
children, adults = [], []

for i, s in enumerate(S):
    if s == "0":
        children.append(W[i])
    else:
        adults.append(W[i])
    W[i] = (W[i], s)
children.sort()
adults.sort()
W.sort()

ans = 0
for w, is_child in W:
    X = w+1 if is_child == "0" else w
    child_num, adult_idx = bisect_right(children, X-1), bisect_left(adults, X)
    adult_num = len(adults) - adult_idx if len(adults) - adult_idx > 0 else 0
    ans = max(ans, child_num+adult_num)
print(ans)
