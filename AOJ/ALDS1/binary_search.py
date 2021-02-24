n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = 0


def binary_search(_list, item):
    low = 0
    high = len(_list)-1

    while low <= high:
        mid = (low + high) // 2
        guess = _list[mid]

        if guess == item:
            return True

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return False


for t in T:
    if binary_search(S, t):
        ans += 1

print(ans)
