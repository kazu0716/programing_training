txt = input()
n = int(input())

for _ in range(n):
    cmd = input().split()
    a, b = int(cmd[1]), int(cmd[2])+1
    if cmd[0] == "replace":
        txt = txt[:a] + cmd[3] + txt[b:]
    elif cmd[0] == "reverse":
        s = txt[a:b]
        txt = txt[:a] + s[::-1] + txt[b:]
    elif cmd[0] == "print":
        print(txt[a:b])
