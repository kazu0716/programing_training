_, K = map(int, input().split())
ans = set([A // K for A in map(int, input().split()) if A % K == 0])
print(*sorted(list(ans)))
