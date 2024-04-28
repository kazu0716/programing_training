N = int(input())
A = list(map(int, input().split()))
stack = []
for a in A:
    stack.append(a)
    while len(stack) >= 2 and stack[-1] == stack[-2]:
        last = stack.pop()
        stack.pop()
        stack.append(last + 1)
print(len(stack))
