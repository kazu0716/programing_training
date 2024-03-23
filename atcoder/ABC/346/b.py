W, B = map(int, input().split())
piano = "wbwbwwbwbwbw"
for i in range(len(piano)):
    w, b = W, B
    while w > 0 or b > 0:
        if piano[i] == "w":
            w -= 1
        else:
            b -= 1
        # NOTE: piano has 12 musical scale
        i = (i + 1) % 12
    if w == b == 0:
        exit(print("Yes"))
print("No")
