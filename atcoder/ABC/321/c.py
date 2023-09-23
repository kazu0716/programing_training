K = int(input())
ans = []
for i in range(0, pow(2, 10)):
    n_list = [j for j, b in enumerate(bin(i)[2:].rjust(10, "0")) if b == "1"]
    n_str = "".join(map(str, sorted(n_list, reverse=True)))
    if n_str:
        ans.append(int(n_str))
print(sorted(ans)[K])
