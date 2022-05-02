from collections import defaultdict
from re import A
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_a, node_b = headA, headB
        while node_a != node_b:
            node_a = headB if not node_a else node_a.next
            node_b = headA if not node_b else node_b.next
        return node_a


if __name__ == "__main__":
    sol = Solution()
    listA = [4, 1, 8, 4, 5]
    listB = [5, 6, 1, 8, 4, 5]
    intersect_val = 8
    head_a = cur_a = ListNode(listA[0])
    head_b = cur_b = ListNode(listB[0])
    inter_section = ListNode(None)
    for i in range(1, len(listA)):
        cur_a.next = ListNode(listA[i])
        if listA[i] == intersect_val:
            inter_section = cur_a.next
            break
        cur_a = cur_a.next
    for i in range(1, len(listB)):
        if listB[i] == intersect_val:
            cur_b.next = inter_section
            cur_b = inter_section
        else:
            cur_b.next = ListNode(listB[i])
            cur_b = cur_b.next
    print(sol.getIntersectionNode(head_a, head_b).val)
