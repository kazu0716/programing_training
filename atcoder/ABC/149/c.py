from math import sqrt

X = int(input())


def is_prime(n):
    for i in range(2, int(sqrt(n))+2):
        if n % i == 0 and i != n:
            return False
    return True


while not is_prime(X):
    X += 1

print(X)
