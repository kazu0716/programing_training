N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
CD = set([tuple(map(int, input().split())) for _ in range(L)])
sorted_B = sorted([(b, i) for i, b in enumerate(B)], reverse=True)
ans = 0
# NOTE: Follow loop process run under O(N + L), because len(CD) is under L
for i, a in enumerate(A):
    for b, j in sorted_B:
        # NOTE: A,B are 0-indexed, but CD is 1-indexed
        if (i + 1, j + 1) not in CD:
            ans = max(ans, (a + b))
            break
print(ans)
