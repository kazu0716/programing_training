N = int(input())
cnt, stack, ans = 0, [], []
for a in list(map(int, input().split())):
    if not stack:
        stack.append([a, 1])
        cnt += 1
    else:
        n, c = stack[-1]
        if n == a:
            if n != c+1:
                stack[-1][1] += 1
                cnt += 1
            else:
                stack.pop()
                cnt -= c
        else:
            stack.append([a, 1])
            cnt += 1
    ans.append(cnt)
print(*ans, sep="\n")
