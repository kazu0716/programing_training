N = int(input())
ST = []

for _ in range(N):
    S, T = input().split()
    T = int(T)
    ST.append((S, T))

sorted_ST = sorted(ST, key=lambda x: x[1])
print(sorted_ST[-2][0])
