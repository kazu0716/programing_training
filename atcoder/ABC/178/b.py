a, b, c, d = map(int, input().split())

ac, ad, = a*c, a*d
bc, bd = b*c, b*d

print(max((ac, ad, bc, bd)))
