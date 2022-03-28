def fibonacci_sum_last_digit(n):
    a, b = 0, 1
    for i in range((n + 2) % 60):
        a, b = b, (a + b) % 10
    return 9 if a == 0 else a - 1


n = int(input())
print(fibonacci_sum_last_digit(n))
