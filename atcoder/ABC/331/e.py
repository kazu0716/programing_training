N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
CD = set([tuple(map(int, input().split())) for _ in range(L)])
sorted_B = sorted([(b, i) for i, b in enumerate(B)], reverse=True)
ans = 0
for i, a in enumerate(A):
    # NOTE: Follow loop process run under O(L)
    for b, j in sorted_B:
        # NOTE: A,B are 0-indexed, but CD is 1-indexed
        if (i + 1, j + 1) not in CD:
            ans = max(ans, (a + b))
            break
print(ans)
