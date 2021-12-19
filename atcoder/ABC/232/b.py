from sys import exit

S, T = input(), input()
dic = list("abcdefghijklmnopqrstuvwxyz")

idx1, idx2 = dic.index(S[0]), dic.index(T[0])
if idx2 - idx1 >= 0:
    diff = idx2 - idx1
else:
    diff = (idx2 + 26 - idx1)

for i in range(1, len(S)):
    if dic[(dic.index(S[i])+diff) % 26] != T[i]:
        print("No")
        exit()

print("Yes")
