i = int(input())
m, s = divmod(i, 60)
h, m = divmod(m, 60)
print("{}:{}:{}".format(h, m, s))
