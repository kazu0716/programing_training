l = list(map(int, input().split()))
W = l[0]
H = l[1]
x = l[2]
y = l[3]
r = l[4]
if (x-r) >= 0 and (y-r) >= 0 and (x+r) <= W and (y+r) <= H:
    print("Yes")
else:
    print("No")
