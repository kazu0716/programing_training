def traverse_tree(pre: int, cur: int, n: int, d: int) -> None:
    global cnt

    while cur >= 1 and d >= 0:
        # NOTE: If the distance from the root is 0, the number of nodes is 1, and finish the recursion.
        if d == 0:
            cnt += 1
            return

        # NOTE: Calculate the number of nodes which are distance d -1  from the target node which is the same level node with pre.
        target = pre + (1 if 2 * cur == pre else - 1)
        cnt += get_num_nodes(target, n, d - 1)

        pre, cur = cur, cur // 2
        d -= 1


def get_num_nodes(root: int, n: int, d: int) -> int:
    # NOTE: d is between 0 and 60, because of depending a number of N is between 1 and 10 ** 18.
    if 0 <= d <= 60:
        left = root * pow(2, d)
        right = min(left + pow(2, d) - 1, n)
        return max(right - left + 1, 0)
    return 0


def solve() -> None:
    global cnt

    T = int(input())
    ans = []
    for _ in range(T):
        N, X, K = map(int, input().split())
        cnt = 0
        # NOTE: Get a number of nodes which are distance K from X and are in the subtree of X.
        cnt += get_num_nodes(X, N, K)
        # NOTE: Traverse binary tree from X to the root.
        traverse_tree(X, X // 2, N, K - 1)
        ans.append(cnt)
    print(*ans, sep="\n")


if __name__ == '__main__':
    solve()
