N = int(input())
ans = set([])

for _ in range(N):
    length, *line = map(int, input().split())
    ans.add(tuple(line))

print(len(ans))
