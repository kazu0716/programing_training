N, K = map(int, input().split())
cnt1 = N // K
if K % 2 == 1:
    print(cnt1 ** 3)
    exit()
cnt2 = N // (K // 2) - cnt1
print(cnt1 ** 3 + cnt2 ** 3)
