from itertools import combinations

while True:
    l = list(map(int, input().split()))
    if l == [0, 0]:
        break
    # NOTE: performance following by Python3, Time:00:79s Memory: 18424KB
    print(len([i for i in list(combinations(range(1, l[0]+1), 3)) if sum(i) == l[1]]))

    # NOTE: performance following by Python3, Time:03:51s Memory: 5604KB
    # r = []
    # n = l[0]
    # x = l[1]
    #
    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         for k in range(1, n+1):
    #             if i + j + k == x and sorted([i, j, k]) not in r and i != j and j != k and i != k:
    #                 r.append([i, j, k])
    # print(len(r))