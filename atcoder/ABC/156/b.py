N = int(input())

cnt1, cnt2 = 0, 0

for A in map(int, input().split()):
    if A % 2 == 0:
        cnt1 += 1
        if A % 3 == 0 or A % 5 == 0:
            cnt2 += 1

if cnt1 == cnt2:
    print("APPROVED")
else:
    print("DENIED")
