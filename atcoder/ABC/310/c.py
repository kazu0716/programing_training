N = int(input())
ans = set()
for _ in range(N):
    S = input()
    if S in ans or S[::-1] in ans:
        continue
    ans.add(S)
print(len(ans))
