from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depth_hash = defaultdict(list)

        def dfs(node, depth):
            if node is None:
                return
            depth_hash[depth].append(node.val)
            for nxt in ((node.left, node.right)):
                dfs(nxt, depth+1)
        if root is None:
            return []
        else:
            dfs(root, 0)
            return [depth_hash[i] for i in range(max(depth_hash.keys())+1)]


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
    print(sol.levelOrder(root))
