import math


def lcm(a, b):
    return int((a / math.gcd(a, b)) * b)


a, b = map(int, input().split())
print(lcm(a, b))
