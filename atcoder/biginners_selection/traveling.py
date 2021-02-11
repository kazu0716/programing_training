def check(t, x, y):
    for i in range(t+1):
        for j in range(t+1):
            if i + j == (t+x+y)/2:
                return True
    return False


def main():
    N = int(input())
    t_0, x_0, y_0 = 0, 0, 0

    for _ in range(N):
        t, x, y = map(int, input().split())
        if check(t-t_0, x-x_0, y-y_0):
            t_0, x_0, y_0 = t, x, y
        else:
            return "No"
    return "Yes"


if __name__ == "__main__":
    print(main())
