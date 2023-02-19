N, K = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(set(A)))[:K]
pre = -1
for b in B:
    if b - 1 != pre:
        print(pre + 1)
        exit()
    pre = b
print(b + 1)
