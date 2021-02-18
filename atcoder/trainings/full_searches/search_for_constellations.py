A, B = [], []

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    A.append((x, y))
A.sort()

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    B.append((x, y))
B.sort()

st_B = set(B)

for b in B:
    cnt = 0
    for a in A:
        vx, vy = a[0] - A[0][0], a[1] - A[0][1]
        if (b[0] + vx, b[1] + vy) in st_B:
            cnt += 1
            if cnt == n:
                dx, dy = b[0] - A[0][0], b[1] - A[0][1]
                print(dx, dy)
                break
    else:
        continue
    break
