# NOTE: solved by Python3
import numpy as np

N, M = map(int, input().split())
A = np.array(list(map(int, input().split()))[::-1])
C = np.array(list(map(int, input().split()))[::-1])

print(*map(int, list(np.polydiv(C, A)[0])[::-1]))
