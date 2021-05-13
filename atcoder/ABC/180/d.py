X, Y, A, B = map(int, input().split())

ans, s = 0, X

while s*A <= Y-1 and (A-1)*s <= B:
    s *= A
    ans += 1

print(ans+(Y-1-s)//B)
