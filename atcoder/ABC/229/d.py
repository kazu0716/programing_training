from bisect import bisect_right

S = input()
K = int(input())

cnt, dots = 0, []
for s in S:
    if s == ".":
        cnt += 1
    dots.append(cnt)

ans = 0
for i in range(len(dots)):
    k = K if i == 0 else dots[i-1]+K
    ans = max(ans, bisect_right(dots, k)-i)

print(ans)
