N, X = map(int, input().split())
S = input()
command = []
for i in range(N):
    if command and command[-1] != "U" and S[i] == "U":
        command.pop()
        continue
    command.append(S[i])

for cmd in command:
    if cmd == "U":
        X //= 2
    else:
        X *= 2
        if cmd == "R":
            X += 1
print(X)
