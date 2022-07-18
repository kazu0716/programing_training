from collections import deque
from sys import setrecursionlimit
from typing import List, Optional

setrecursionlimit(pow(10, 9))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time complexity : O(N)
        Space complexity : O(1)
        """
        def dfs(node, depth):
            if not node:
                return
            if len(view) == depth:
                view.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        view = []
        dfs(root, 0)
        return view


def convert_list_to_bst(nums: Optional[List[Optional[int]]]) -> Optional[TreeNode]:
    if nums is None:
        return None
    stack = nums[::-1]
    root = TreeNode(val=stack.pop())
    queue = deque([root])
    while queue:
        node = queue.popleft()
        try:
            val = stack.pop()
            if val is not None:
                node.left = TreeNode(val=val)
                queue.append(node.left)
            val = stack.pop()
            if val is not None:
                node.right = TreeNode(val=val)
                queue.append(node.right)
        except IndexError:
            break
    return root


if __name__ == "__main__":
    sol = Solution()
    # root = [1, 2, 3, None, 5, None, 4]
    root = [1, 2, 3, 4]
    head = convert_list_to_bst(root)
    print(sol.rightSideView(head))
