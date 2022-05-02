from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None


def list_to_tree(l: list) -> Optional[TreeNode]:
    if not l:
        return None
    root = TreeNode(l[0])
    queue, idx = deque([root]), 0
    while queue:
        cur = queue.popleft()
        if idx+1 >= len(l):
            break
        cur.left = TreeNode(l[idx+1])
        if idx+2 >= len(l):
            break
        cur.right = TreeNode(l[idx+2])
        idx += 2
        queue.append(cur.left)
        queue.append(cur.right)
    return root


if __name__ == "__main__":
    sol = Solution()
    root = [4, 2, 7, 1, 3, 6, 9]
    print(sol.invertTree(list_to_tree(root)).val)
