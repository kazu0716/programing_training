import queue

l = []
n = int(input())
q = queue.LifoQueue()

for i in list(map(int, input().split())):
    q.put(i)

while not q.empty():
    l.append(q.get())

print(" ".join(map(str, l)))
