from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        val = 0
        if root1:
            val += root1.val
        if root2:
            val += root2.val
        root = TreeNode(val=val)
        queue = deque([(root, root1, root2)])
        while queue:
            node, node1, node2 = queue.popleft()
            for i in range(2):
                if i == 0:
                    nxt1 = node1.left if node1 else None
                    nxt2 = node2.left if node2 else None
                else:
                    nxt1 = node1.right if node1 else None
                    nxt2 = node2.right if node2 else None
                if not nxt1 and not nxt2:
                    continue
                val = 0
                if nxt1:
                    val += nxt1.val
                if nxt2:
                    val += nxt2.val
                nxt = TreeNode(val=val)
                if i == 0:
                    node.left = nxt
                else:
                    node.right = nxt
                queue.append((nxt, nxt1, nxt2))
        return root
