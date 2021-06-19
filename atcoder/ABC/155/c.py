N = int(input())
dic = {}

for _ in range(N):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

s = max(dic.values())
ans = []

for k, v in dic.items():
    if s == v:
        ans.append(k)

print(*sorted(ans), sep="\n")
