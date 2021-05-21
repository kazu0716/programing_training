N = int(input())
A = list(map(int, input().split()))

boss = [0] * N

for a in A:
    boss[a-1] += 1

print(*boss, sep="\n")
