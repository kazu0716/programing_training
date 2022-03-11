from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry, val = (l1.val+l2.val)//10, (l1.val+l2.val) % 10
        head = cur = ListNode(val=val)
        while l1.next or l2.next:
            n = carry
            if l1.next:
                n += l1.next.val
                l1 = l1.next
            if l2.next:
                n += l2.next.val
                l2 = l2.next
            carry, val = n//10, n % 10
            cur.next = ListNode(val=val)
            cur = cur.next
        if carry != 0:
            cur.next = ListNode(val=carry)
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
    linked_list1, linked_list2 = LinkedList(), LinkedList()
    for linked_list in (linked_list1, linked_list2):
        input_list = list(map(int, list(input().replace("[", "").replace("]", "").split(","))))
        for n in input_list:
            linked_list.add(n)
    solution.addTwoNumbers(linked_list1.get_head(), linked_list2.get_head())
    linked_list.show()
