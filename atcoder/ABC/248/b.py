A, B, K = map(int, input().split())
if A == B:
    print(0)
    exit()
for i in range(1, 100):
    A *= K
    if A >= B:
        print(i)
        exit()
