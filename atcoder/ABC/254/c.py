from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
if K == 1:
    print("Yes")
    exit()
dict_set = defaultdict(lambda: defaultdict(int))
for i, a in enumerate(A):
    dict_set[i % K][a] += 1
A.sort()
for i, a in enumerate(A):
    if dict_set[i % K][a] > 0:
        dict_set[i % K][a] -= 1
    else:
        print("No")
        exit()
print("Yes")
