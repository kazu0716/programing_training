ans = False

X, Y = map(int, input().split())
for x in range(X+1):
    if 2*x + 4*(X-x) != Y:
        continue
    ans = True
    break

if ans:
    print("Yes")
else:
    print("No")
