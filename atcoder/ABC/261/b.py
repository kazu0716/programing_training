N = int(input())
A = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if not((A[i][j] == "L" and A[j][i] == "W") or (A[i][j] == "W" and A[j][i] == "L") or (A[i][j] == A[j][i] == "D")):
            print("incorrect")
            exit()
print("correct")
