from sys import setrecursionlimit
from typing import List, Optional

setrecursionlimit(pow(10, 9))


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create_bst(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            mid_idx = (left_idx + right_idx) // 2
            node = TreeNode(val=nums[mid_idx])
            node.left = create_bst(left_idx, mid_idx - 1)
            node.right = create_bst(mid_idx + 1, right_idx)
            return node
        return create_bst(0, len(nums)-1)


if __name__ == "__main__":
    sol = Solution()
    nums = [-10, -3, 0, 5, 9]
    # nums = [1, 2, 3, 4]
    root = sol.sortedArrayToBST(nums)
    print(root.val)
    print(root.left.val)
    print(root.right.val)
