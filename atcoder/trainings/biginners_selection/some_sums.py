ans = []
N, A, B = map(int, input().split())

for i in range(N+1):
    sum_ = 0
    for c in list(str(i)):
        sum_ += int(c)
    if sum_ >= A and sum_ <= B:
        ans.append(i)

print(sum(ans))
