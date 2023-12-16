SS = "".join(sorted(input()))
TT = "".join(sorted(input()))
len_1 = ["AB", "AE", "BC", "CD", "DE"]
len_2 = ["AC", "AD", "BD", "BE", "CE"]
if (SS in len_1 and TT in len_1) or (SS in len_2 and TT in len_2):
    print("Yes")
else:
    print("No")
