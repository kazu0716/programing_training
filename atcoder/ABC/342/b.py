N = int(input())
P = list(map(int, input().split()))
Q = int(input())
ans = []
for _ in range(Q):
    A, B = map(int, input().split())
    pos_a, pos_b = P.index(A), P.index(B)
    ans.append(A if pos_a < pos_b else B)
print(*ans, sep="\n")
