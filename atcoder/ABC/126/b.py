S = input()

date1 = int(S[:2])
date2 = int(S[2:])

if 1 <= date1 and date1 <= 12 and 1 <= date2 and date2 <= 12:
    print("AMBIGUOUS")
elif 1 <= date1 and date1 <= 12:
    print("MMYY")
elif 1 <= date2 and date2 <= 12:
    print("YYMM")
else:
    print("NA")
