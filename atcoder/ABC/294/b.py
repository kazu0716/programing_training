H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
print(*["".join(["." if n == 0 else chr(64 + n) for n in A[i]]) for i in range(H)], sep="\n")
