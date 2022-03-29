from collections import deque
from token import OP
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ordered_list = []

        def dfs(node):
            nonlocal ordered_list
            if node is None:
                return
            dfs(node.left)
            ordered_list.append(node.val)
            dfs(node.right)
        dfs(root)
        return ordered_list


def convert_list_to_bst(nums: Optional[List[Optional[int]]]) -> Optional[TreeNode]:
    if nums is None:
        return None
    stack = nums[::-1]
    root = TreeNode(val=stack.pop())
    queue = deque([root])
    while queue:
        node = queue.popleft()
        try:
            val = stack.pop()
            if val is not None:
                node.left = TreeNode(val=val)
                queue.append(node.left)
            val = stack.pop()
            if val is not None:
                node.right = TreeNode(val=val)
                queue.append(node.right)
        except IndexError:
            break
    return root


if __name__ == "__main__":
    sol = Solution()
    root = convert_list_to_bst([1, None, 2, 3])
    print(sol.inorderTraversal(root))
