O = [[-1 for _ in range(15)] for _ in range(15)]
N = int(input())
ans = 0

for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        O[i][x-1] = y


for n in range(2 ** N):
    bit = bin(n)[2:].rjust(N, "0")
    flag = True
    for i in range(N):
        if bit[i] == "1":
            for j in range(N):
                if O[i][j] != -1 and O[i][j] != int(bit[j]):
                    flag = False

    if flag:
        ans = max(bit.count("1"), ans)

print(ans)
