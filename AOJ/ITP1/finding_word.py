w = input()
ans = 0

while True:
    txt = input()
    if txt == "END_OF_TEXT":
        break
    for s in txt.split():
        if s.lower() == w.lower():
            ans += 1
print(ans)
