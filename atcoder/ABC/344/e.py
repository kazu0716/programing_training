from collections import defaultdict


class Node(object):
    """Doubly Linked List Node"""

    def __init__(self, val, pre, nxt):
        self.val = val
        self.pre = pre
        self.nxt = nxt


N = int(input())
A = list(map(int, input().split()))
# NOTE: get node from value
# because A always has unique value under this problem
pos = defaultdict(Node)
# NOTE: create doubly-linked-list from list of python with pos
pre, cur = None, None
for a in A:
    cur, pre = Node(a, cur, None), cur
    if pre is not None:
        pre.nxt = cur
    pos[a] = cur
Q = int(input())
for _ in range(Q):
    q = tuple(map(int, input().split()))
    target_node = pos[q[1]]
    nxt_node = target_node.nxt
    if q[0] == 1:
        # NOTE: connect target_node <-> new_node <-> nxt_node
        new_node = Node(q[2], target_node, nxt_node)
        target_node.nxt = new_node
        if nxt_node is not None:
            nxt_node.pre = new_node
        # NOTE: update node
        pos[q[2]] = new_node
    else:
        pre_node = target_node.pre
        # NOTE: delete target_node, so this list becomes pre_node <-> nxt_node
        if pre_node is not None:
            pre_node.nxt = nxt_node
        if nxt_node is not None:
            nxt_node.pre = pre_node
        # NOTE: delete node
        del pos[target_node.val]
# NOTE: find root from pos, because a root node don't have pre_node
root = None
for k in pos:
    if pos[k].pre is None:
        root = pos[k]
        break
ans = []
while root is not None:
    ans.append(root.val)
    root = root.nxt
print(*ans)
