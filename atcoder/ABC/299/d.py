N = int(input())
left, right = 0, 1
left_index, right_index = 1, N
for _ in range(20):
    mid_index = (left_index + right_index) // 2
    print("?", mid_index)
    mid = int(input())
    if left != mid:
        right = mid
        right_index = mid_index
    else:
        left = mid
        left_index = mid_index
    if abs(right_index - left_index) == 1:
        print("!", left_index)
        exit()
