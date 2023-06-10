p, q = input().split()
p_idx, q_idx = ord(p) - ord("A"), ord(q) - ord("A")
if p_idx > q_idx:
    p_idx, q_idx = q_idx, p_idx
dis = (3, 1, 4, 1, 5, 9)
ans = 0
for i in range(p_idx, q_idx):
    ans += dis[i]
print(ans)
