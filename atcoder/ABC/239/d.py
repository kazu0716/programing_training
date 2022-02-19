from math import sqrt


def get_sieve_of_eratosthenes(n):
    prime = []
    limit = sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


A, B, C, D = map(int, input().split())
prime, cnt = set(get_sieve_of_eratosthenes(200)), 0
for i in range(A, B+1):
    flag = False
    for j in range(C, D+1):
        if i+j in prime:
            flag = True
            break
    if flag:
        cnt += 1
if cnt == B-A+1:
    print("Aoki")
else:
    print("Takahashi")
