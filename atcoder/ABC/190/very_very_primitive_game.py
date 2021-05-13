A, B, C = map(int, input().split())

if C == 0:
    if A >= B+1:
        print("Takahashi")
    else:
        print("Aoki")
else:
    if B >= A+1:
        print("Aoki")
    else:
        print("Takahashi")
