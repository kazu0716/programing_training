_ = int(input())
H = list(map(int, input().split()))
num, h = 0, 0
for i, height in enumerate(H):
    if height > h:
        num, h = i, height
print(num+1)
