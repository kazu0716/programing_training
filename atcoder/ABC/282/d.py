from collections import deque
from enum import Enum
from typing import Dict, List, Optional, Set


class Color(Enum):
    RED = "red"
    BLUE = "blue"


def paint_bipartite_graph(root: int) -> Optional[Dict[Color, Set[int]]]:
    colors: Dict[Color, Set[int]] = {Color.RED: set([root]), Color.BLUE: set()}
    queue = deque([(root, Color.RED)])
    while queue:
        cur_pos, cur_color = queue.popleft()
        visited[cur_pos] = True
        for nxt_pos in G[cur_pos]:
            # NOTE: isn't bipartite graph
            if nxt_pos in colors[cur_color]:
                return None
            nxt_color = Color.BLUE if cur_color == Color.RED else Color.RED
            # NOTE: check visited node or not
            if nxt_pos not in colors[nxt_color]:
                colors[nxt_color].add(nxt_pos)
                queue.append((nxt_pos, nxt_color))
    return colors


N, M = map(int, input().split())
G: List[List[int]] = [[] for _ in range(N)]
visited = {i: False for i in range(N)}
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)

ans = N * (N - 1) // 2
for i in range(N):
    if visited[i]:
        continue
    # NOTE: avoid to search same graph, and so add None to graph_colors when the graph isn't bipartite graph
    colors = paint_bipartite_graph(i)
    if colors is None:
        print(0)
        exit()
    red_cnt, blue_cnt = len(colors[Color.RED]), len(colors[Color.BLUE])
    # ref: https://twitter.com/kyopro_friends/status/1604113410983342080/photo/1
    ans -= red_cnt * (red_cnt - 1) // 2
    ans -= blue_cnt * (blue_cnt - 1) // 2
print(ans - M)
