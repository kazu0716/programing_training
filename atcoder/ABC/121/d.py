def f(a, b):
    cnt = b - a + 1
    return cnt // 2 % 2 if cnt % 2 == 0 else (cnt // 2 % 2) ^ b


A, B = map(int, input().split())
print(f(0, A - 1) ^ f(0, B))
