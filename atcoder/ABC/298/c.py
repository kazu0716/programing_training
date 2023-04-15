from collections import defaultdict

N = int(input())
Q = int(input())
box = defaultdict(list)
card, card_set = defaultdict(list), defaultdict(set)
for _ in range(Q):
    query = list(map(int, input().split()))
    i = query[1]
    if query[0] == 1:
        j = query[2]
        box[j].append(i)
        if j not in card_set[i]:
            card[i].append(j)
            card_set[i].add(j)
    elif query[0] == 2:
        print(*sorted(box[i]))
    else:
        print(*sorted(card[i]))
