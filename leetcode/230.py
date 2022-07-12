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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        def dfs(node: TreeNode):
            return dfs(node.left) + [node.val] + dfs(node.right) if node else []
        return dfs(root)[k-1]

    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time complexity : O(log N + k)
        Space complexity : O(log N)
        """
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            # NOTE: root equals minium value node
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


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
    root = [5, 3, 6, 2, 4, None, None, 1]
    k = 3
    head = convert_list_to_bst(root)
    print(sol.kthSmallest2(head, k))
