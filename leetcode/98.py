from collections import deque
from sys import setrecursionlimit
from typing import List, Optional

setrecursionlimit(pow(10, 9))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    INF = pow(10, 18)

    def isValidBST(self, root, left=-INF, right=INF):
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False
        return self.isValidBST(root.left, left, root.val) and self.isValidBST(root.right, root.val, right)


def convert_list_to_bst(nums: Optional[List[int]]) -> Optional[TreeNode]:
    if nums is None:
        return None
    stack = nums[::-1]
    root = TreeNode(val=stack.pop())
    queue = deque([root])
    while queue:
        node = queue.popleft()
        try:
            node.left = TreeNode(val=stack.pop())
            queue.append(node.left)
            node.right = TreeNode(val=stack.pop())
            queue.append(node.right)
        except Exception:
            break
    return root


if __name__ == "__main__":
    sol = Solution()
    tree = convert_list_to_bst([120, 70, 140, 50, 100, 130, 160, 20, 55, 75, 110, 119, 135, 150, 200])
    print(sol.isValidBST(tree))
