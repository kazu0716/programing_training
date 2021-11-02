from collections import defaultdict
from sys import exit

N = int(input())
tasks = defaultdict(list)

for _ in range(N):
    A, B = map(int, input().split())
    tasks[B].append(A)

t = 0
for key in sorted(tasks.keys()):
    while tasks[key]:
        t += tasks[key].pop()
        if t > key:
            print("No")
            exit()

print("Yes")
