# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        str1, nxt1 = [], l1
        while nxt1 is not None:
            str1 += str(nxt1.val)
            nxt1 = nxt1.next
        str1 = int("".join(str1[::-1]))

        str2, nxt2 = [], l2
        while nxt2 is not None:
            str2 += str(nxt2.val)
            nxt2 = nxt2.next
        str2 = int("".join(str2[::-1]))

        ans = None
        for s in str(str1 + str2):
            if ans is None:
                nxt = None
            else:
                nxt = ans
            ans = ListNode(val=s, next=nxt)

        return ans
