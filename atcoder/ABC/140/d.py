N, K = map(int, input().split())
S = input()

line = []
pre, cnt = S[0], 1
for i in range(1, len(S)):
    if pre == S[i]:
        cnt += 1
    else:
        line.append([len(line), pre, cnt])
        cnt = 1
    pre = S[i]
line.append([len(line), pre, cnt])

sorted_line = sorted(line, key=lambda x: x[2])
for _ in range(K):
    if not sorted_line:
        break
    idx, direction, n = sorted_line.pop()
    line[idx][1] = "R" if direction == "L" else "L"

ans = 0
for _ in range(len(line)):
    idx, direction, n = line.pop()
    if not line:
        ans += n-1
        break
    if line[-1][1] == direction:
        line[-1][2] += n
    else:
        ans += n-1

print(ans)
