from collections import defaultdict

N, Q = map(int, input().split())
bowl, pos = [], defaultdict(int)
for i in range(N):
    pos[i+1] = i
    bowl.append(i+1)
for _ in range(Q):
    x = int(input())
    x_pos = pos[x]
    x1_pos = x_pos + 1 if 0 <= x_pos + 1 < N else x_pos - 1
    x1 = bowl[x1_pos]
    bowl[x_pos], bowl[x1_pos] = bowl[x1_pos], bowl[x_pos]
    pos[x], pos[x1] = x1_pos, x_pos
print(*bowl)
