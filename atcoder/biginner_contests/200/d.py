N = int(input())
n = min(N, 8)
A = list(map(int, input().split()))[0:n]
q_list = [[] for _ in range(200)]


def solve():
    for i in range(1, 2 ** n):
        bit = bin(i)[2:].rjust(n, "0")
        s, l = 0, []
        for i, b in enumerate(list(bit)):
            if b != "1":
                continue
            s += A[i]
            l.append(i+1)
        idx = s % 200
        q_list[idx].append(l)
        if len(q_list[idx]) >= 2:
            return idx
    return None


ans = solve()
if ans is None:
    print("No")
else:
    print("Yes")
    x, y = q_list[ans][1], q_list[ans][0]
    print(*([len(x)]+x))
    print(*([len(y)]+y))
