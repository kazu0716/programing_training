from itertools import combinations

H1, W1 = map(int, input().split())
A = [list(input().split()) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(input().split()) for _ in range(H2)]

for hc in combinations(range(H1), H2):
    for wc in combinations(range(W1), W2):
        is_A_eq_B = True
        for i, h in enumerate(hc):
            for j, w in enumerate(wc):
                if B[i][j] != A[h][w]:
                    is_A_eq_B = False
                    break
            else:
                continue
            break
        if is_A_eq_B:
            print("Yes")
            exit()
print("No")
