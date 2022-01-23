N, M = map(int, input().split())
S = set(list(input().split()))
T = set(list(input().split()))

for s in S:
    if s in T:
        print("Yes")
    else:
        print("No")
