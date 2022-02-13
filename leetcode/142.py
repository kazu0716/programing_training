import logging
from typing import Optional
from unittest import main


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, node = head, set()
        while cur:
            if cur in node:
                return cur
            node.add(cur)
            cur = cur.next
        return None


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
        if pos < 0:
            logging.error("pos has to be positive number.")
            return
        cnt, cur = 0, self.head
        dep, end = None, None
        while cur:
            if cnt == pos:
                target = cur
            dep = cur
            cur = cur.next
            cnt += 1
        if not dep or not target:
            logging.error("Couldn't create loop.")
            return
        dep.next = target

    def show(self) -> None:
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

    def get_pos_node(self) -> Optional[ListNode]:
        """
        Use Floyd’s Cycle-Finding Algorithm

        Time complexity: O(n)
        Auxiliary Space: O(1)
        """
        # NOTE: adopt for leetcode
        head = self.head
        # NOTE: following LeetCode solution
        if not head:
            return None
        slow = head.next
        if not slow:
            return None
        fast = slow.next
        while slow != fast:
            if not slow or not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
        while head != slow:
            head, slow = head.next, slow.next
        return head


if __name__ == "__main__":
    row = input()
    input_list = list(map(int, list(row.replace("[", "").replace("]", "").split(",")))) if row != "[]" else None
    pos = int(input())
    solution = Solution()
    linked_list = LinkedList()
    print("input", input_list)
    if input_list:
        print("== add data to Linked List ==")
        for n in input_list:
            linked_list.add(n)
        print("== show data in Linked List ==")
        linked_list.show()
        print("== create loop in Linked List ==")
        linked_list.create_loop(pos)
    print("== solution ==")
    print(linked_list.get_pos_node().val)
