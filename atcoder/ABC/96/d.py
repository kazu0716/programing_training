N = int(input())
limit = 55555
is_prime = [True] * (limit + 1)
ans = []
for i in range(2, limit + 1):
    if not is_prime[i]:
        continue
    if i % 5 == 1:
        ans.append(i)
    if len(ans) >= N:
        exit(print(*ans))
    for j in range(2 * i, limit + 1, i):
        is_prime[j] = False
