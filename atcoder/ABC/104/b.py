from collections import Counter

S = input()
print("AC" if S[0] == "A" and S.replace("A", "").replace("C", "").islower() and Counter(S[2:-1])["C"] == 1 else "WA")
