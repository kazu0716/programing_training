S1, S2, S3, S4 = input(), input(), input(), input()

penciles = ["H", "2B", "3B", "HR"]
ans = [S1, S2, S3, S4]

if sorted(penciles) == sorted(ans):
    print("Yes")
else:
    print("No")
