from collections import defaultdict

S = input()
T = input()
cnt_s = defaultdict(int)
cnt_t = defaultdict(int)
keys = set()
for s, t in zip(S, T):
    cnt_s[s] += 1
    cnt_t[t] += 1
    keys.add(s)
    keys.add(t)
keys.discard("@")
for k in keys:
    if cnt_t[k] == cnt_s[k]:
        continue
    if k not in "atcoder":
        print("No")
        exit()
    if cnt_t[k] > cnt_s[k]:
        cnt_s["@"] -= cnt_t[k] - cnt_s[k]
    else:
        cnt_t["@"] -= cnt_s[k] - cnt_t[k]
    if cnt_s["@"] < 0 or cnt_t["@"] < 0:
        print("No")
        exit()
print("Yes")
