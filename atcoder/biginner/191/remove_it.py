N, X = map(int, input().split())
A = list(map(int, input().split()))

print(" ".join([str(i) for i in A if i != X]))