import sys
from collections import deque
from typing import Optional

sys.setrecursionlimit(pow(10, 9))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dis = 0

        def dfs(node) -> int:
            nonlocal dis
            if node is None:
                return 0
            l_dep, r_dep = dfs(node.left), dfs(node.right)
            dis = max(dis, l_dep + r_dep)
            return 1 + max(l_dep, r_dep)

        dfs(root)
        return dis


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
    tree = [1, 2, 3, 4, 5]
    root = list_to_tree(tree)
    sol = Solution()
    print(sol.diameterOfBinaryTree(root))
