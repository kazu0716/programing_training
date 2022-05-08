N, A, B = map(int, input().split())

field = []
for i in range(A*N):
    width = []
    for j in range(B*N):
        if ((i // A) % 2 == 0 and (j // B) % 2 == 0) or ((i // A) % 2 != 0 and (j // B) % 2 != 0):
            width.append(".")
        else:
            width.append("#")
    field.append(width)

for f in field:
    print(*f, sep="")
