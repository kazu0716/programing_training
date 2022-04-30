from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def add(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val)
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(val)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            head = cur = list1
            list1 = list1.next
        else:
            head = cur = list2
            list2 = list2.next
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next, list1 = list1, list1.next
            else:
                cur.next, list2 = list2, list2.next
            cur = cur.next
        if list1 or list2:
            cur.next = list1 if list1 else list2
        return head


def show(head) -> None:
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next


if __name__ == "__main__":
    sol = Solution()
    list1 = [1, 2, 4]
    ll1 = LinkedList()
    for l1 in list1:
        ll1.add(l1)
    list2 = [1, 3, 4]
    ll2 = LinkedList()
    for l2 in list2:
        ll2.add(l2)
    head = sol.mergeTwoLists(ll1.get_head(), ll2.get_head())
    show(head)
