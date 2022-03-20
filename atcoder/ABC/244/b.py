N = int(input())
T = input()

direction = ((1, 0), (0, -1), (-1, 0), (0, 1))
cnt = 0
pos = [0, 0]
for i in range(N):
    d = T[i]
    if d == "S":
        dd = direction[cnt % 4]
        pos[0] += dd[0]
        pos[1] += dd[1]
    else:
        cnt += 1
print(*pos)
