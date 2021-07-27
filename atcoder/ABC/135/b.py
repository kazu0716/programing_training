N = int(input())
P = list(map(int, input().split()))

arr = list(range(1, N+1))
l = []

for i in range(N):
    if arr[i] == P[i]:
        continue
    l.append(i)

cnt = len(l)

if cnt < 2:
    print("YES")
elif cnt == 2:
    idx1, idx2 = l[0], l[1]
    p1, p2 = P[idx1], P[idx2]
    P[idx1], P[idx2] = p2, p1
    if P == arr:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
