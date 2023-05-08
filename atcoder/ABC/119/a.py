def to_day(y, m, d):
    return y * 365 * 31 + m * 31 + d


S = input()
dates = tuple(map(int, S.split("/")))
print("Heisei" if to_day(2019, 4, 30) >= to_day(*dates) else "TBD")
