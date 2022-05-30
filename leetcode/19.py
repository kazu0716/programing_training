from heapq import heappop, heappush
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time complexity : O(n)
        Space complexity : O(1)

        ref: https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions
        """
        fast = slow = head
        # NOTE: proceed for step n times
        for _ in range(n):
            fast = fast.next
        # NOTE: when n equals linkedlist length, delete head
        if fast is None:
            return head.next
        # NOTE: proceed for slow until n+1 th node
        while fast.next:
            slow, fast = slow.next, fast.next
        # NOTE: delete nth node
        slow.next = slow.next.next
        return head


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
    head = [1]
    n = 1
    root = list_to_linked_list(head)
    print(sol.removeNthFromEnd(root, n))
