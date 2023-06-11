def get_nxt_node(v):
    for nxt in v:
        if nxt in visited:
            continue
        stack.append(nxt)
        visited.add(nxt)
        return nxt
    # NOTE: remove a node which already has been finished searching
    stack.pop()
    # NOTE: search previous node
    return stack[-1]


N, M = map(int, input().split())
stack = [1]
visited = set([1])
while stack:
    ans = input().split()
    if ans[0] == "OK" or ans == "-1":
        exit()
    print(get_nxt_node(tuple(map(int, ans))[1:]))
