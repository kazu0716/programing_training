D = int(input())
N = int(input())
attendances = [0] * (D + 2)
for _ in range(N):
    L, R = map(int, input().split())
    attendances[L] += 1
    attendances[R + 1] -= 1
for i in range(len(attendances) - 1):
    attendances[i + 1] += attendances[i]
print(*attendances[1:-1], sep="\n")
