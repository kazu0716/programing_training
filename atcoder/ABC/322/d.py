from copy import deepcopy
from typing import List, Optional

H = W = 4


def trim_graph(p: List[List[str]]) -> List[List[str]]:
    """Trim graph null lines and rows."""
    pop_h_set, pop_w_set = set(), set()
    for i in range(H):
        if p[i] == ["."] * W:
            pop_h_set.add(i)
    rotated_p = rotate_graph(p, 1)
    for j in range(W):
        if rotated_p[j] == ["."] * H:
            pop_w_set.add(j)
    ret = []
    for i in range(H):
        if i in pop_h_set:
            continue
        row = []
        for j in range(W):
            if j in pop_w_set:
                continue
            row.append(p[i][j])
        ret.append(row)
    return ret


def get_field(i: int, j: int, field: List[List[str]], graph: List[List[str]]) -> Optional[List[List[str]]]:
    for k in range(len(graph)):
        for _l in range(len(graph[0])):
            h, w = i + k, j + _l
            if not (0 <= h < H and 0 <= w < W) or field[h][w] == graph[k][_l] == "#":
                return None
            field[h][w] = "." if field[h][w] == graph[k][_l] == "." else "#"
    return field


def get_moved_graph_field(field: List[List[str]], graph: List[List[str]]) -> List[List[List[str]]]:
    ret = []
    for i in range(H):
        for j in range(W):
            f = get_field(i, j, deepcopy(field), graph)
            if f is not None:
                ret.append(f)
    return ret


def rotate_graph(graph: List[List[str]], code: int) -> List[List[str]]:
    """Rotate graph 90 degrees clockwise by code."""
    if code == 0:
        return graph
    elif code == 1:
        return [list(g) for g in zip(*graph[::-1])]
    elif code == 2:
        return [list(g) for g in list(zip(*graph))[::-1]]
    elif code == 3:
        return [list(gg) for gg in [g[::-1] for g in graph][::-1]]
    else:
        raise Exception("Invalid code")


def main() -> None:
    P1 = [list(input()) for _ in range(H)]
    P2 = [list(input()) for _ in range(H)]
    P3 = [list(input()) for _ in range(H)]
    TARGET = [["#"] * W for _ in range(H)]
    CODE_NUM = 4
    rotated_trimmed_p2 = [rotate_graph(trim_graph(P2), c) for c in range(CODE_NUM)]
    rotated_trimmed_p3 = [rotate_graph(trim_graph(P3), c) for c in range(CODE_NUM)]
    for f1 in get_moved_graph_field([["."] * W for _ in range(H)], trim_graph(P1)):
        for rotated_p2 in rotated_trimmed_p2:
            for f2 in get_moved_graph_field(f1, rotated_p2):
                for rotated_p3 in rotated_trimmed_p3:
                    for f3 in get_moved_graph_field(f2, rotated_p3):
                        if f3 == TARGET:
                            exit(print("Yes"))
    print("No")


if __name__ == '__main__':
    main()
