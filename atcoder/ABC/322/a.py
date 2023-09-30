N = int(input())
S = input()
ans = S.find("ABC")
print(ans + (1 if ans > -1 else 0))
