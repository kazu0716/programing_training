N = int(input())
P = list(map(int, input().split()))
cnt = [0] * N
for i, p in enumerate(P):
    # NOTE: For now, a cuisine of p is front of person i, but we should turn the table for satisfying someone by p
    turn_num = (p - i) % N
    cnt[turn_num] += 1
    cnt[(turn_num - 1) % N] += 1
    cnt[(turn_num + 1) % N] += 1
print(max(cnt))
