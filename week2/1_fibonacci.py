from math import sqrt


def fib(n):
    result = (((1 + sqrt(5)) ** n) - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))
    return int(result)


n = int(input())
print(fib(n))
