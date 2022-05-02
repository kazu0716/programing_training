from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = None
        while slow:
            nxt = slow.next
            tail, slow.next = slow, tail
            slow = nxt
        while head and tail:
            if head.val != tail.val:
                return False
            head, tail = head.next, tail.next
        return True


def list_to_linked_list(l: list) -> Optional[ListNode]:
    if not l:
        return None
    root = cur = ListNode(l[0])
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next
    return root


if __name__ == "__main__":
    sol = Solution()
    head = [1, 1, 1, 2, 2, 1, 1, 1]
    print(sol.isPalindrome(list_to_linked_list(head)))
