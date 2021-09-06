contests = [input() for _ in range(3)]

for contest in ("ABC", "ARC", "AGC", "AHC"):
    if contest not in contests:
        print(contest)
        break
