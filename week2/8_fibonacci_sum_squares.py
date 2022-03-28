def fib(f, n):
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10
    return f


def fib_last_digit(n):
    f = [0] * 61
    f = fib(f, 60)
    return f[n % 60]


def fibonacci_sum_squares(n):
    vertical_side = fib_last_digit(n)
    horizontal_side = fib_last_digit((n + 1))
    return (vertical_side * horizontal_side) % 10


n = int(input())
print(fibonacci_sum_squares(n))
