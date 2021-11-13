N = int(input())

ans = 0
for a in range(1, int(pow(N, 1/3)+2)):
    for b in range(a, int(pow(N, 1/2))+2):
        if a*pow(b, 2) > N:
            break
        ans += N//(a*b) - b + 1

print(ans)
