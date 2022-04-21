import logging
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if slow.next is None:
                return False
            slow = slow.next
            for _ in range(2):
                if fast.next is None:
                    return False
                fast = fast.next
        return True


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val)
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(val)

    def create_loop(self, pos: int) -> None:
        """
        pos is 0-indexed
        """
        if pos == 0:
            Exception("Couldn't create self-loop")
        cnt, cur = 0, self.head
        dep, end = None, None
        while cur:
            if cnt == pos:
                target = cur
            dep = cur
            cur = cur.next
            cnt += 1
        if dep is None or target is None:
            Exception("Couldn't create loop")
        dep.next = target

    def show(self) -> None:
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

    def get_head(self) -> Optional[ListNode]:
        return self.head


sol = Solution()
l = LinkedList()
test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for t in test:
    l.add(t)
l.create_loop(9)
print(sol.hasCycle(l.get_head()))
