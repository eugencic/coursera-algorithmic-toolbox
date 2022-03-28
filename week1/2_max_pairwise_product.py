# from random import randint
#
#
# def max_pairwise_product_naive(arr):
#     product = 0
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             product = max(product, arr[i] * arr[j])
#     return product


def max_pairwise_product_fast(arr):
    n1 = max(arr)
    arr.remove(n1)
    n2 = max(arr)
    return n1 * n2


# def stress_test(n1, n2):
#     while True:
#         n = randint(2, n1)
#         arr = [None] * n
#         for i in range(n):
#             arr[i] = randint(0, n2)
#         print(arr)
#         result1 = max_pairwise_product_naive(arr)
#         result2 = max_pairwise_product_fast(arr)
#         if result1 == result2:
#             print('OK')
#         else:
#             print('Wrong answer:', result1, result2)
#             return


# stress_test(5, 50)

input_n = int(input())
input_numbers = [int(x) for x in input().split()]
print(max_pairwise_product_fast(input_numbers))
