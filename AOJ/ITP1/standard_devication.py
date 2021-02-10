from statistics import pstdev

data = []

while True:
    n = int(input())
    if n == 0:
        break
    data.append(list(map(int,input().split())))

for d in data:
    print(pstdev(d))