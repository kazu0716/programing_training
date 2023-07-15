_, P, Q = map(int, input().split())
D = tuple(map(int, input().split()))
print(min(P, Q + min(D)))
