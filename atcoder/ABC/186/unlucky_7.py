N = int(input())
ans = 0

for i in range(1, N+1):
    i_8 = oct(i)
    i_10 = str(i)
    if "7" not in i_8 and "7" not in i_10:
        ans += 1

print(ans)
