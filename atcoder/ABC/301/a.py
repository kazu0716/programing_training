N = int(input())
S = input()
t_cnt, a_cnt = 0, 0
for i in range(N):
    if S[i] == "T":
        t_cnt += 1
        continue
    a_cnt += 1
if t_cnt == a_cnt:
    print("T" if S[-1] == "A" else "A")
    exit()
print("T" if t_cnt > a_cnt else "A")
