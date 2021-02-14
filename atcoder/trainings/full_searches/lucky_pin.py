N = int(input())
S = input()

ans = 0

for p in [str(i).zfill(3) for i in range(1000)]:
    p_0 = S.find(p[0])
    p_1 = S.find(p[1], p_0+1)
    p_2 = S.find(p[2], p_1+1)
    if p_0 >= 0 and p_1 > p_0 and p_2 > p_1:
        ans += 1

print(ans)
