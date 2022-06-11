X, A, D, N = map(int, input().split())
if D < 0:
    A, D = A + (N-1)*D, -D
if X <= A:
    print(abs(X-A))
    exit()
if X >= A+(N-1)*D:
    print(abs(X-(A+(N-1)*D)))
    exit()
low, high = 1, N
while low <= high:
    mid = (low+high) // 2
    if A+(mid-1)*D == X:
        print(0)
        exit()
    elif A+(mid-1)*D > X:
        high = mid - 1
    else:
        low = mid + 1
print(min(abs((A+(low-1)*D)-X), abs((A+(high-1)*D)-X)))
