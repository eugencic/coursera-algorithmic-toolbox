def fibonacci_partial_sum(m, n):
    if m > n:
        return

    a = [0, 1]
    for i in range(2, 60):
        a.append(a[i - 1] + a[i - 2])

    m = m % 60
    n = n % 60
    if n < m:
        n += 60

    sum = 0
    for j in range(m, n + 1):
        sum += a[j % 60]

    return sum % 10


source, destination = map(int, input().split())
print(fibonacci_partial_sum(source, destination))
