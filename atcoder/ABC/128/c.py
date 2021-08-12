N, M = map(int, input().split())
switches = []

for _ in range(M):
    ks = list(map(int, input().split()))
    switches.append(ks[1:])

P = list(map(int, input().split()))

ans = 0

for i in range(pow(2, N)):
    cnt1 = 0
    bit = bin(i)[2:].rjust(N, "0")
    for j in range(M):
        cnt2 = 0
        switch = switches[j]
        for s in switch:
            if bit[s - 1] == "1":
                cnt2 += 1
        if cnt2 % 2 == P[j]:
            cnt1 += 1

    if cnt1 == M:
        ans += 1

print(ans)
