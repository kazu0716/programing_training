def sum_xor(x):
    return (x + 1) // 2 % 2 if (x + 1) % 2 == 0 else ((x + 1) // 2 % 2) ^ x


A, B = map(int, input().split())
print(sum_xor(A - 1) ^ sum_xor(B))
