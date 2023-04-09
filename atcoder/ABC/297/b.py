S = input()
print("Yes" if (S.find("B") - S.rfind("B")) % 2 == 1 and S.find("R") < S.find("K") < S.rfind("R") else "No")
