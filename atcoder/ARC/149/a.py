N, M = map(int, input().split())
mod_list, d = [[0]*9 for _ in range(N)], range(1, 10)
for i in range(N):
    for j in d:
        mod_list[i][j-1] = j % M if i == 0 else (10 * mod_list[i-1][j-1] + j) % M
for i in range(N-1, -1, -1):
    for j in d[::-1]:
        if mod_list[i][j-1] == 0:
            print(str(j)*(i+1))
            exit()
print(-1)
