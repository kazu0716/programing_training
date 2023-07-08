from operator import itemgetter

N, K = map(int, input().split())
medicines = []
n = 0
for _ in range(N):
    a, b = map(int, input().split())
    medicines.append((a, b))
    n += b
medicines.sort(reverse=True, key=itemgetter(0))
ans = 1
while medicines and n > K:
    a, b = medicines.pop()
    ans = a + 1
    n -= b
print(ans)
