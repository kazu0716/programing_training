S = input()

flag = False

for i in range(len(S)-1):
    s1, s2 = S[i], S[i+1]
    if s1 == s2:
        flag = True
        break

if flag:
    print("Bad")
else:
    print("Good")
