from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ini = -200
        pre, cur = ListNode(ini), head
        while cur:
            nxt, flag = cur.next, True
            while nxt and cur.val == nxt.val:
                nxt = nxt.next
                flag = False
            if flag and pre.val != cur.val:
                if pre.val == ini:
                    head, cur.next = cur, nxt
                    pre, cur = cur, nxt
                else:
                    pre.next, cur.next = cur, nxt
                    pre, cur = cur, nxt
            if not flag and not nxt:
                pre.next = None
                if pre.val == ini:
                    head = None
            cur = nxt
        return head


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

    def get_head(self) -> Optional[ListNode]:
        return self.head

    def show(self, head) -> None:
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next


if __name__ == "__main__":
    solution = Solution()
    linked_list = LinkedList()
    input_list = list(map(int, list(input().replace("[", "").replace("]", "").split(","))))
    for n in input_list:
        linked_list.add(n)
    linked_list.show(solution.deleteDuplicates(linked_list.get_head()))
