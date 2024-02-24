from collections import Counter

S = input()
cnt = Counter(S)
for k, v in cnt.items():
    if v == 1:
        exit(print(S.index(k) + 1))
