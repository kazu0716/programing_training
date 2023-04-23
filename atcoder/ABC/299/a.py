N = int(input())
S = input()
print("in" if S.find("|") < S.find("*") < S.rfind("|") else "out")
