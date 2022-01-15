from sys import exit

a, N = map(int, input().split())

finds = [False]*pow(10, len(str(N))+1)
finds[N] = True
cur, ans = set([N]), 0

while cur:
    next = set([])
    for n in cur:
        if n % a == 0:
            nxt = n//a
            if nxt == 1:
                print(ans+1)
                exit()
            next.add(nxt)
        sn = str(n)
        if n > 10 and sn[1] != "0":
            next.add(int(sn[1:]+sn[0]))
    cur = set([])
    for nxt in next:
        if not finds[nxt]:
            cur.add(nxt)
            finds[nxt] = True
    ans += 1

print(-1)
