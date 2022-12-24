from collections import defaultdict

S = input()
cnt, box, boxes = 0, defaultdict(int), [defaultdict(int)]
for s in S:
    if s == "(":
        boxes.append(defaultdict(int))
        cnt += 1
    elif s == ")":
        if cnt <= 0:
            continue
        cnt -= 1
        removes = boxes.pop()
        for key in removes:
            box[key] -= removes[key]
            if box[key] <= 0:
                del box[key]
    else:
        if s in box:
            print("No")
            exit(0)
        boxes[-1][s] += 1
        box[s] += 1
print("Yes")
