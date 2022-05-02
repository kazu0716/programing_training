from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array_list = []
        while head:
            array_list.append(head.val)
            head = head.next
        for i in range(len(array_list)//2+1):
            if array_list[i] != array_list[len(array_list)-1-i]:
                return False
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
    head = [1, 2, 2, 1]
    print(sol.isPalindrome(list_to_linked_list(head)))
