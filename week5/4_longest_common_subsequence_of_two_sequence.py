def lcs(X, Y, m, n):
    l = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i - 1][j], l[i][j - 1])
    return l[m][n]


n = int(input())
str1 = input().split()
n1 = int(input())
str2 = input().split()
print(lcs(str1, str2, n, n1))
