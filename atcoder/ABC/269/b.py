S = [list(input()) for _ in range(10)]
i_min, i_max = 10, 0
j_min, j_max = 10, 0
for i in range(10):
    for j in range(10):
        if S[i][j] == ".":
            continue
        i_min, i_max = min(i_min, i), max(i_max, i)
        j_min, j_max = min(j_min, j), max(j_max, j)
print(i_min+1, i_max+1)
print(j_min+1, j_max+1)
