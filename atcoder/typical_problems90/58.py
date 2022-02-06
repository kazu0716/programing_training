N, K = map(int, input().split())
MAX1, MAX2 = pow(10, 5), 60

dv = [[0]*MAX1 for _ in range(MAX2)]
dv[0] = [(i+sum(map(int, list(str(i))))) % MAX1 for i in range(MAX1)]

for i in range(1, MAX2):
    for j in range(MAX1):
        dv[i][j] = dv[i-1][dv[i-1][j]]

bit = list(bin(K)[2:])[::-1]
for j in [i for i in range(len(bit)) if bit[i] == "1"]:
    N = dv[j][N]
print(N)
