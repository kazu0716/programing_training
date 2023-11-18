N, Q = map(int, input().split())
C = list(map(int, input().split()))
box = [set([c]) for c in C]
ans = []
for _ in range(Q):
    a, b = map(int, input().split())
    box_a, box_b = box[a - 1], box[b - 1]
    if len(box_b) < len(box_a):
        box_a, box_b = box_b, box_a
    for c in box_a:
        if c not in box_b:
            box_b.add(c)
    box[a - 1], box[b - 1] = set(), box_b
    ans.append(len(box_b))
print(*ans, sep='\n')
