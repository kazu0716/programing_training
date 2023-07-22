N = int(input())
S = input()
print(max(S.find(c) for c in "ABC") + 1)
