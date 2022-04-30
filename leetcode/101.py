from collections import deque
from sys import setrecursionlimit
from typing import Optional

setrecursionlimit(pow(10, 9))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        if root.left is None or root.right is None or root.left.val != root.right.val:
            return False
        left_list, right_list = [], []

        def dfs(node, direction):
            nonlocal left_list, right_list
            if node is None:
                if direction == "left":
                    left_list.append(None)
                else:
                    right_list.append(None)
                return
            if direction == "left":
                left_list.append(node.val)
                dfs(node.left, direction)
                dfs(node.right, direction)
            else:
                right_list.append(node.val)
                dfs(node.right, direction)
                dfs(node.left, direction)

        dfs(root.left, "left")
        dfs(root.right, "right")
        return tuple(left_list) == tuple(right_list)


if __name__ == "__main__":
    sol = Solution()
    root = [1, 2, 2, None, 3, None, 3]
    root_node = list_to_binary_tree(root)
    print(sol.isSymmetric(root_node))
