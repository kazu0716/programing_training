l = list(map(int, input().split()))
d = l[0]//l[1]
r = l[0] % l[1]
f = l[0]/l[1]
print("{} {} {:.06f}".format(d, r, f))
