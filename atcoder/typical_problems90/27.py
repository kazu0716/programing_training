N = int(input())
users, ans = set([]), []

for i in range(N):
    S = input()
    if S in users:
        continue
    users.add(S)
    ans.append(i+1)

print(*ans, sep="\n")
