from sys import setrecursionlimit
from typing import Optional

setrecursionlimit(pow(10, 9))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth: int = 0

        def dfs(node: TreeNode, d: int) -> None:
            nonlocal depth
            for nxt_node in (node.left, node.right):
                if not nxt_node:
                    depth = max(depth, d)
                    continue
                dfs(nxt_node, d+1)
        if root:
            dfs(root, 1)
        return depth


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=1, left=None, right=TreeNode(val=2))
    print(sol.maxDepth(root))
