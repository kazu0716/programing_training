S = input()
if S[0] == "1":
    print("No")
    exit()
is_standings = [False] * 7
if S[6] == "1":
    is_standings[0] = True
if S[3] == "1":
    is_standings[1] = True
if S[7] == "1" or S[1] == "1":
    is_standings[2] = True
if S[0] == "1" or S[4] == "1":
    is_standings[3] = True
if S[2] == "1" or S[8] == "1":
    is_standings[4] = True
if S[5] == "1":
    is_standings[5] = True
if S[9] == "1":
    is_standings[6] = True
cur, status = 1, is_standings[0]
# NOTE: compress is_staindings to ease to compare answer
while cur < len(is_standings):
    if is_standings[cur] == status:
        is_standings.pop(cur)
    else:
        status = is_standings[cur]
        cur += 1
# NOTE: actually, range(len(is_standings)-3 + 1)
for i in range(len(is_standings)-2):
    if [is_standings[i], is_standings[i+1], is_standings[i+2]] == [True, False, True]:
        print("Yes")
        exit()
print("No")
