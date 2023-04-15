def is_array_eq(a, b):
    for i in range(N):
        for j in range(N):
            if a[i][j] == "1" and b[i][j] != "1":
                return False
    return True


N = int(input())
A = [tuple(input().split()) for _ in range(N)]
B = [tuple(input().split()) for _ in range(N)]
A_right90 = list(zip(*A[::-1]))
A_right180 = list(zip(*A_right90[::-1]))
A_right270 = list(zip(*A_right180[::-1]))
for arr in (A, A_right90, A_right180, A_right270):
    if is_array_eq(arr, B):
        print("Yes")
        exit()
print("No")
