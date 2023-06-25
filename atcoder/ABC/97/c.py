s = input()
K = int(input())
s_set = set()
for i in range(len(s)):
    for j in range(1, 6):
        s_set.add(s[i:i + j])
print(sorted(list(s_set))[K - 1])
