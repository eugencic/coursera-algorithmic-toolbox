import numpy


def lcs(s1, s2, s3, n1, n2, n3):
    matrix = numpy.zeros((n1 + 1, n2 + 1, n3 + 1))

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            for k in range(1, n3 + 1):
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    matrix[i][j][k] = matrix[i - 1][j - 1][k - 1] + 1
                else:
                    matrix[i][j][k] = max(matrix[i - 1][j][k], matrix[i][j - 1][k], matrix[i][j][k - 1])

    return int(matrix[-1][-1][-1])


n = int(input())
str1 = input().split()

n1 = int(input())
str2 = input().split()

n2 = int(input())
str3 = input().split()
print(lcs(str1, str2, str3, n, n1, n2))
