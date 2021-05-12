N = int(input())

ans = [0, 0, 0, 0]

for _ in range(N):
    s = input()
    if s == "AC":
        ans[0] += 1
    elif s == "WA":
        ans[1] += 1
    elif s == "TLE":
        ans[2] += 1
    elif s == "RE":
        ans[3] += 1

print("AC x {}".format(str(ans[0])))
print("WA x {}".format(str(ans[1])))
print("TLE x {}".format(str(ans[2])))
print("RE x {}".format(str(ans[3])))
