import sys

S = input()
T = list("oxx"*30)

while len(T) > len(S):
    if S == "".join(T[0:len(S)]):
        print("Yes")
        sys.exit()
    T.pop(0)

print("No")
