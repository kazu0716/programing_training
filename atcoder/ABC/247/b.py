from collections import defaultdict

N = int(input())
names, name_hash = [], defaultdict(int)
for _ in range(N):
    s, t = input().split()
    name_hash[s] += 1
    name_hash[t] += 1
    names.append((s, t))

for s, t in names:
    name_hash[s] -= 1
    name_hash[t] -= 1
    if name_hash[s] > 0 and name_hash[t] > 0:
        print("No")
        exit()
    name_hash[s] += 1
    name_hash[t] += 1
print("Yes")
