from collections import deque
from heapq import heappop, heappush
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        nums = [root.val]

        def dfs(node: TreeNode):
            nonlocal nums
            if node.left is not None:
                nums.append(node.left.val)
                dfs(node.left)
            if node.right is not None:
                nums.append(node.right.val)
                dfs(node.right)

        dfs(root)
        nums.sort()
        return nums[k-1]


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
    root = [3, 1, 4, None, 2]
    # root = [1]
    k = 1
    head = convert_list_to_bst(root)
    print(sol.kthSmallest(head, k))
