A, B, W = map(float, input().split())

ans = [n for n in range(1, pow(10, 6)+1) if A * n <=
       W * 1000 and W * 1000 <= B * n]

if len(ans) > 0:
    print(min(ans), max(ans))
else:
    print("UNSATISFIABLE")
