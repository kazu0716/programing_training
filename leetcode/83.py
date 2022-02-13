from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur_node = head
        while cur_node:
            if not cur_node.next:
                break
            nxt_node = cur_node.next
            while nxt_node and cur_node.val == nxt_node.val:
                nxt_node = nxt_node.next
                cur_node.next = nxt_node
            cur_node = nxt_node
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

    def show(self) -> None:
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next


if __name__ == "__main__":
    solution = Solution()
    linked_list = LinkedList()
    input_list = list(map(int, list(input().replace("[", "").replace("]", "").split(","))))
    for n in input_list:
        linked_list.add(n)
    solution.deleteDuplicates(linked_list.get_head())
    linked_list.show()
