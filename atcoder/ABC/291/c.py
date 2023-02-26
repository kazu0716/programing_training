N = int(input())
S = input()
pos_x, pos_y = 0, 0
pos_set = set([(0, 0)])
for s in S:
    if s == "R":
        pos_x += 1
    elif s == "L":
        pos_x -= 1
    elif s == "U":
        pos_y += 1
    else:
        pos_y -= 1
    if (pos_x, pos_y) in pos_set:
        print("Yes")
        exit()
    pos_set.add((pos_x, pos_y))
print("No")
