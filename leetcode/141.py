import logging
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Use hash table

        Time complexity: O(n)
        Auxiliary Space: O(n)
        """
        cur, s = head, set([])
        while cur:
            if cur in s:
                return True
            s.add(cur)
            cur = cur.next
        return False


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

    def is_loop(self) -> bool:
        """
        Use Floyd’s Cycle-Finding Algorithm

        Time complexity: O(n)
        Auxiliary Space: O(1)
        """
        if not self.head:
            return False
        slow: ListNode = self.head
        fast: Optional[ListNode] = self.head.next if self.head else None
        step: int = 2
        while slow != fast:
            if not slow or not fast:
                return False
            slow = slow.next
            for _ in range(step):
                fast = fast.next
                if not fast:
                    return False
        return True


s = Solution()
l = LinkedList()
test = [3, 2, 0, -4]
for t in test:
    l.add(t)
l.create_loop(1)
print(l.is_loop())
