N = int(input())
w_list = [input() for _ in range(N)]
w_set = set(w_list)
if len(w_list) != len(w_set):
    print("No")
    exit()
for i in range(N - 1):
    cur, nxt = w_list[i], w_list[i + 1]
    if cur[-1] != nxt[0]:
        print("No")
        exit()
print("Yes")
