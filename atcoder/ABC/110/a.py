A, B, C = map(int, input().split())
sorted_list = sorted([A, B, C])
print(sorted_list[2] * 10 + sorted_list[0] + sorted_list[1])
