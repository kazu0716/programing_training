N, _ = map(int, input().split())
PCF = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    p1, f1 = PCF[i][0], set(PCF[i][2:])
    for j in range(N):
        if i == j:
            continue
        p2, f2 = PCF[j][0], set(PCF[j][2:])
        if p1 >= p2 and f1 <= f2 and (p1 > p2 or f1 < f2):
            exit(print("Yes"))
print("No")
