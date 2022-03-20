N = int(input())
s = set([])
while True:
    for i in range(1, 2*N+2):
        if i not in s:
            print(i)
            s.add(i)
            break
    aoki = int(input())
    if aoki == 0:
        break
    s.add(aoki)
