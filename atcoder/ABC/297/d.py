A, B = map(int, input().split())
if A == B:
    print(0)
    exit()
if A > B:
    A, B = B, A
cnt = 0
while A > 0 and A < B:
    cnt += B // A
    A, B = B % A, A
print(cnt - 1)
