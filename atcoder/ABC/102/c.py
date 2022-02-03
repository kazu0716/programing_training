from statistics import median

N = int(input())
A = list(map(int, input().split()))
B = []
for i, a in enumerate(A):
    B.append(a-i-1)
B.sort()
b = median(B)
ans = 0
for i, a in enumerate(A):
    ans += abs(a-(b+(i+1)))
print(ans)
