N = int(input())
S = input()

for i in range(N):
    s = S[i]
    if s == "1" and i % 2 == 0:
        print("Takahashi")
        break
    elif s == "1" and i % 2 != 0:
        print("Aoki")
        break
