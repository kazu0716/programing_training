from hashlib import sha256


def hash_sum(n):
    ret = 0
    for s in sha256(str(n).encode()).hexdigest():
        ret += ord(s)
    return ret


N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

set_A, len_A, sum_A = set([A[0]]), [1], [hash_sum(A[0])]
for i in range(1, N):
    sum_A.append(sum_A[i-1] + (hash_sum(A[i]) if A[i] not in set_A else 0))
    set_A.add(A[i])
    len_A.append(len(set_A))
set_B, len_B, sum_B = set([B[0]]), [1], [hash_sum(B[0])]
for i in range(1, N):
    sum_B.append(sum_B[i-1] + (hash_sum(B[i]) if B[i] not in set_B else 0))
    set_B.add(B[i])
    len_B.append(len(set_B))

Q = int(input())
ans = []
for _ in range(Q):
    x, y = map(int, input().split())
    if len_A[x-1] == len_B[y-1] and sum_A[x-1] == sum_B[y-1]:
        ans.append("Yes")
    else:
        ans.append("No")
print(*ans, sep="\n")
