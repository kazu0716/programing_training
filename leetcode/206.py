from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack, cur = [], head
        while cur and cur.next:
            stack.append(cur)
            cur = cur.next
        tail = cur
        while stack:
            nxt = stack.pop()
            cur.next = nxt
            cur = nxt
        cur.next = None
        return tail


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
    head = solution.reverseList(linked_list.get_head())
    linked_list.show(head)
