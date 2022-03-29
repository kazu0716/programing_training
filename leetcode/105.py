from collections import defaultdict, deque
from sys import setrecursionlimit
from typing import List, Optional

setrecursionlimit(pow(10, 9))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_idx = 0

        def list_to_tree(left_idx: int, right_idx: int) -> Optional[TreeNode]:
            nonlocal preorder_idx
            if left_idx > right_idx:
                return None
            val = preorder[preorder_idx]
            root = TreeNode(val=val)
            preorder_idx += 1
            root.left = list_to_tree(left_idx, inorder_dict[val]-1)
            root.right = list_to_tree(inorder_dict[val]+1, right_idx)
            return root

        inorder_dict = defaultdict(int)
        for i, n in enumerate(inorder):
            inorder_dict[n] = i
        return list_to_tree(0, len(inorder)-1)


def tree_to_list(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    tree_list = []
    queue = deque([root])
    while queue:
        same_depth = []
        for _ in range(len(queue)):
            node = queue.popleft()
            same_depth.append(None if node is None else node.val)
            if node is None:
                continue
            for nxt in (node.left, node.right):
                queue.append(nxt)
        if same_depth.count(None) < len(same_depth):
            tree_list += same_depth
    return tree_list


if __name__ == "__main__":
    sol = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = sol.buildTree(preorder, inorder)
    print(tree_to_list(root))
