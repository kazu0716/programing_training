V, T, S, D = map(int, input().split())

t = D / V

if T > t or t > S:
    print("Yes")
else:
    print("No")
