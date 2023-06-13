from functools import reduce

N = int(input())
A = list(map(int, input().split()))
print(reduce(lambda x, y: x + y - 1, A) - 1)
