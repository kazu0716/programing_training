from bisect import bisect_left

N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        c_max = L[i]+L[j]
        k = bisect_left(L, c_max)-1
        ans += k-j

print(ans)
