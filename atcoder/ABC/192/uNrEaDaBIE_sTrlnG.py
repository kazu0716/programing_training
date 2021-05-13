S = list(input())

flag = True

for i, s in enumerate(S):
    if not(((i+1) % 2 == 1 and s.islower()) or ((i+1) % 2 == 0 and s.isupper())):
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
