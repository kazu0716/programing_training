N = int(input())
name = []
root, age = 0, pow(10, 18)
for i in range(N):
    S, A = input().split()
    name.append(S)
    if int(A) < age:
        root, age = i, int(A)
print(*(name[root:] + name[:root]), sep="\n")
