from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        flag = False

        def dfs(node, cost):
            nonlocal flag
            if node.left is None and node.right is None:
                if cost == targetSum:
                    flag = True
                return
            for nxt in ((node.left, node.right)):
                if nxt is None:
                    continue
                dfs(nxt, cost + nxt.val)
        if root is None:
            return False
        else:
            dfs(root, root.val)
            return flag


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
    target_sum = 5
    print(sol.hasPathSum(root, target_sum))
