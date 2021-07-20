N = int(input())
dic, ans = {}, 0

for _ in range(N):
    s = "".join(sorted(list(input())))
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

for k in dic:
    ans += (dic[k] * (dic[k] - 1))//2

print(ans)
