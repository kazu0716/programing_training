def func(x):
    return x**2 + 2*x + 3


t = int(input())
print(func(func(func(t)+t)+func(func(t))))
