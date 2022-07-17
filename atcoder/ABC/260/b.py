N, X, Y, Z = map(int, input().split())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

ans = set()
math, english, total = [], [], []
for i in range(N):
    math.append((A[i], -i))
    english.append((B[i], -i))
    total.append((A[i]+B[i], -i))
math.sort(reverse=True)
english.sort(reverse=True)
total.sort(reverse=True)
for threshold, score in ((X, math), (X+Y, english), (X+Y+Z, total)):
    pos = 0
    while len(ans) < threshold:
        ans.add(-score[pos][1]+1)
        pos += 1
print(*sorted(list(ans)), sep="\n")
