from collections import defaultdict

N, M = map(int, input().split())
city_dict = defaultdict(list)
for i in range(M):
    P, Y = map(int, input().split())
    city_dict[P].append((Y, i))
ans = []
for p in city_dict:
    city_dict[p].sort()
    for i, v in enumerate(city_dict[p]):
        n = v[1]
        _id = str(p).rjust(6, "0") + str(i + 1).rjust(6, "0")
        ans.append((n, _id))
ans.sort()
print(*[_id for _, _id in ans], sep="\n")
