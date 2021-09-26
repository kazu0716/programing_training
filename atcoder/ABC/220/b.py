K = int(input())
A, B = map(int, (input().split()))


def convert(n, k):
    result, cnt = 0, 0
    for i in list(str(n))[::-1]:
        result += int(i) * pow(k, cnt)
        cnt += 1
    return result


print(convert(A, K)*convert(B, K))
