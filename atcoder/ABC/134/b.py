N, D = map(int, input().split())

ans = N/(2*D+1)

if ans % 1 == 0:
    print(int(ans))
else:
    print(int(ans+1))
