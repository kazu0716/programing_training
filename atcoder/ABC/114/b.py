S = input()
ans = pow(10, 18)
for i in range(len(S) - 2):
    x = int(S[i:i + 3])
    ans = min(ans, abs(x - 753))
print(ans)
