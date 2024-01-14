X = int(input())
print((X & -X).bit_length() - 1)
