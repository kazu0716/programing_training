from collections import deque
from sys import setrecursionlimit
from typing import Optional

setrecursionlimit(pow(10, 9))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            cur, depth = queue.popleft()
            if not cur.left and not cur.right:
                return depth
            for nxt in (cur.left, cur.right):
                if not nxt:
                    continue
                queue.append((nxt, depth+1))


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=1, left=None, right=TreeNode(val=2))
    print(sol.minDepth(root))
