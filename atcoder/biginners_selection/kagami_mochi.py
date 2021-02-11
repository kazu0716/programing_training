N = int(input())
D = [int(input()) for _ in range(N)]

D.sort(reverse=True)
ans = []

pre = float("inf")

for d in D:
    if d < pre:
        ans.append(d)
        pre = d

print(len(ans))
