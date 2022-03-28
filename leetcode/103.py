from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        depth_list = []
        queue = deque([root])
        while queue:
            nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth_list.append(nodes)
        return [depth[::-1] if i % 2 != 0 else depth for i, depth in enumerate(depth_list)]


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
    print(sol.zigzagLevelOrder(root))
