n = int(input())
t = [int(i) for i in input().split()]


def is_greater_or_equal(digit, max_digit):
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))


def largest_number(lst):
    answer = []

    while lst:
        max_digit = 0
        for digit in lst:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer


print(''.join([str(i) for i in largest_number(t)]))
