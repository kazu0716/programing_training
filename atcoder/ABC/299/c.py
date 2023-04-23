N = int(input())
S = input().split("-")
l = len(max(S))
print(l if l > 0 and len(S) > 1 else -1)
