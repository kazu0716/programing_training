X = int(input())

q1, mod1 = divmod(X, 500)
ans = 1000*q1
ans += 5*(mod1//5)

print(ans)
