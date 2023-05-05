A, B, C, D, E = int(input()), int(input()), int(input()), int(input()), int(input())
t = 0
dishes = sorted([A, B, C, D, E], key=lambda x: x % 10 if x % 10 != 0 else x, reverse=True)
for i, d in enumerate(dishes):
    t += d
    if t % 10 == 0 or i == 4:
        continue
    t = (t // 10 + 1) * 10
print(t)
