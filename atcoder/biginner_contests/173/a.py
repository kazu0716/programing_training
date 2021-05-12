N = int(input())

q = N // 1000
if N % 1000 == 0:
    print(0)
else:
    print(1000*(q+1)-N)
