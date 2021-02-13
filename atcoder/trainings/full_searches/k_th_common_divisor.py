A, B, K = map(int, input().split())

ans = [i for i in range(1, 1+max(A, B)) if A % i == 0 and B % i == 0]
ans.sort(reverse=True)
print(ans[K-1])
