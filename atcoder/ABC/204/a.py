x, y = map(int, input().split())

if x == y:
    print(x)
else:
    ans = [0, 1, 2]
    ans.remove(x)
    ans.remove(y)
    print(ans[0])
