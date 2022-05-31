from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        pre, cur, root = None, head, head.next
        while cur and cur.next:
            nxt = cur.next
            if pre:
                pre.next = nxt
            cur.next, nxt.next = nxt.next, cur
            pre, cur = cur, cur.next
        return root


def list_to_linked_list(l: list) -> Optional[ListNode]:
    if not l:
        return None
    root = cur = ListNode(l[0])
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next
    return root


def print_linked_list(node: ListNode) -> None:
    cnt = 1
    while node:
        print(cnt, node.val)
        cnt += 1
        node = node.next


if __name__ == "__main__":
    sol = Solution()
    head = [1, 2, 3, 4]
    root = list_to_linked_list(head)
    print_linked_list(sol.swapPairs(root))
