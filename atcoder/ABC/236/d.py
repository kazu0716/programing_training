def solve(member, score):
    if not member:
        global ans
        ans = max(ans, score)
        return
    i = member[0]
    for j in range(1, len(member)):
        m = member.copy()
        m.remove(i)
        m.remove(member[j])
        solve(m, score ^ A[i][member[j]])


N = int(input())
A = [[0]*(2*N) for _ in range(2*N-1)]

for i in range(2*N-1):
    for j, v in enumerate(list(map(int, input().split()))):
        A[i][i+j+1] = v
ans = 0
solve([i for i in range(2*N)], 0)
print(ans)
