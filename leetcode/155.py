from collections import defaultdict
from heapq import heappop, heappush


class MinStack:

    def __init__(self):
        self.stack = []
        self.dict = defaultdict(int)
        self.heap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.dict[val] += 1
        heappush(self.heap, val)

    def pop(self) -> None:
        self.dict[self.stack.pop()] -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        mi = heappop(self.heap)
        while self.dict[mi] == 0:
            mi = heappop(self.heap)
        heappush(self.heap, mi)
        return mi


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.top())
    print(min_stack.getMin())
