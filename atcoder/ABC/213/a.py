A, B = map(int, input().split())

for i in range(2**8):
    if A ^ i == B:
        print(i)
        break
