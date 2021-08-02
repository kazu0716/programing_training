N = int(input())
D = list(map(int, input().split()))
D.sort()

n1, n2 = D[N//2-1], D[N//2]
print(n2-n1)
