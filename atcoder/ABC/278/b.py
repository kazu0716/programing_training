H, M = map(int, input().split())
cur_hour = H * 60 + M
for _ in range(60 * 24 + 1):
    h, m = map(str, divmod(cur_hour, 60))
    h, m = h.rjust(2, "0"), m.rjust(2, "0")
    changed_h, changed_m = int(h[0] + m[0]), int(h[1] + m[1])
    if 0 <= changed_h <= 23 and 0 <= changed_m <= 59:
        print(h, m)
        exit()
    cur_hour += 1
    cur_hour %= 60 * 24
