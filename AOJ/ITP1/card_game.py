score = [0, 0]
n = int(input())


def compare(taro, hanako):
    i = 0
    while True:
        try:
            taro_s = ord(taro[i])
            hanako_s = ord(hanako[i])
            if taro_s > hanako_s:
                return True
            elif hanako_s > taro_s:
                return False
            else:
                i += 1
        except IndexError:
            if len(taro) > len(hanako):
                return True
            else:
                return False


for _ in range(n):
    taro, hanako = input().split()
    if taro == hanako:
        score[0] += 1
        score[1] += 1
    else:
        if compare(taro, hanako):
            score[0] += 3
        else:
            score[1] += 3
print(*score)
