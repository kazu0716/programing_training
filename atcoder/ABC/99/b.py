a, b = map(int, input().split())
h = [1]
for i in range(2, 1000):
    h.append(h[-1] + i)
    if h[-2] - a == h[-1] - b:
        print(h[-2] - a)
        exit()
