N = input()

flag = True

cnt = 0

for i in range(1, len(N)):
    if N[-i] == "0":
        cnt += 1
    else:
        break

S = "0"*cnt + N

for i in range(len(S)):
    if S[i] != S[-i-1]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
