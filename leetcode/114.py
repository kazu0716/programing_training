from collections import deque
from sys import setrecursionlimit
from typing import Optional

setrecursionlimit(pow(10, 6))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        Time complexity: O(n)
        Auxiliary Space: O(n)
        """
        if root is None:
            return

        nodes = [root]

        def dfs(cur):
            nonlocal nodes
            if cur.left:
                nodes.append(cur.left)
                dfs(cur.left)
            if cur.right:
                nodes.append(cur.right)
                dfs(cur.right)

        dfs(root)
        for i in range(len(nodes)-1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1]


def list_to_binary_tree(tree_list: list) -> Optional[TreeNode]:
    if not list:
        return None
    pos = 0
    root = node = TreeNode(val=tree_list[pos])
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        if pos+1 >= len(tree_list):
            break
        cur.left = None if tree_list[pos+1] is None else TreeNode(val=tree_list[pos+1])
        if pos+2 >= len(tree_list):
            break
        cur.right = None if tree_list[pos+2] is None else TreeNode(val=tree_list[pos+2])
        pos += 2
        queue.append(cur.left)
        queue.append(cur.right)
    return root


if __name__ == "__main__":
    sol = Solution()
    root = [1, 2, 5, 3, 4, None, 6]
    head = list_to_binary_tree(root)
    sol.flatten(head)
