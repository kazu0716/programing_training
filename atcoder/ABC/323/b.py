N = int(input())
cnt = []
for _ in range(N):
    S = input()
    cnt.append(S.count("x"))
print(*[i for _, i in sorted([(c, i + 1) for i, c in enumerate(cnt)])], sep="\n")
