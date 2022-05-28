H, W = map(int, input().split())

pos = []
for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == "o":
            pos.append((i, j))
print(abs(pos[0][0]-pos[1][0])+abs(pos[0][1]-pos[1][1]))
