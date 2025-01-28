from re import sub

S = input()
S = sub("[A]+", "1", S)
S = sub("[B]+", "2", S)
S = sub("[C]+", "3", S)
print("Yes" if S in {"1", "2", "3", "12", "23", "13", "123"} else "No")
