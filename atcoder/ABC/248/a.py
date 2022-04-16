S = input()
int_list = [i for i in range(10)]
for s in S:
    if int(s) in int_list:
        int_list.remove(int(s))
print(int_list[0])
