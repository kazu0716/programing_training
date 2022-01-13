S = "0b" + input()

s1 = int("0b" + "".join(["0" if i %
         2 == 0 else "1" for i in range(len(S)-2)]), 2)
s2 = int("0b" + "".join(["1" if i %
         2 == 0 else "0" for i in range(len(S)-2)]), 2)

print(min(bin(int(S, 2) ^ s1)[2:].count("1"),
      bin(int(S, 2) ^ s2)[2:].count("1")))
