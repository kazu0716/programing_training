for i in range(8):
    S = input()
    for j, s in enumerate(S):
        if s == "*":
            print("abcdefgh"[j], 8 - i, sep="")
