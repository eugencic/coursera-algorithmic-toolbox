def gold(x, w, n):
    l = [[0 for h in range(n + 1)] for tsg in range(w + 1)]
    for j in range(1, n + 1):
        for i in range(1, w + 1):
            if i == x[j]:
                l[i][j] = i
            else:
                l[i][j] = l[i][j - 1]
                if x[j] <= i:
                    val = l[i - x[j]][j - 1] + x[j]
                    if l[i][j] < val:
                        l[i][j] = val
    return l[w][n]


iii = list(map(int, input().split()))
W, N = iii[0], iii[1]
X = list(map(int, input().split()))
if 0 not in X:
    X.append(0)
X.sort()
print(gold(X, W, N))
