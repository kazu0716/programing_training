from string import ascii_lowercase

N = int(input())
S = input()
Q = int(input())
alt = {c: c for c in ascii_lowercase}
for _ in range(Q):
    c, d = input().split()
    for k, v in alt.items():
        if v == c:
            alt[k] = d
print(*[alt[s] for s in S], sep="")
