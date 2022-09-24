def get_non_rook_pos(axis: str) -> int:
    T, low, high = 0, 1, N
    while T != -1 and high - low > 0:
        mid = (low + high) // 2
        if axis == "X":
            print("?", low, mid, 1, N)
        else:
            print("?", 1, N, low, mid)
        T = int(input())
        if T <= mid - low:
            high = mid
        else:
            low = mid + 1
    return low


N = int(input())
print("!", get_non_rook_pos("X"), get_non_rook_pos("Y"))
