from collections import deque

N = int(input())
V = list(map(int, input().split()))
V.sort()

queue = deque(V)

for _ in range(N-1):
    a = queue.popleft()
    b = queue.popleft()
    queue.appendleft((a+b)/2)

print(queue.pop())
