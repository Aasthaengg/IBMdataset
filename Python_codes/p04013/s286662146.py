N, A = [int(_) for _ in input().split()]

MAX_I = 5000
memo = [[0] * MAX_I for _ in range(N + 2)]


def cnv(v):
    return v - A + (MAX_I // 2)


X = [int(_) for _ in input().split()]
for i in range(N):
    offset = X[i] - A
    # print('x', offset)

    mm = memo[i]
    for j in range(MAX_I):
        if mm[j] > 0:
            memo[i + 1][j + offset] += mm[j]
        memo[i + 1][j] += mm[j]

    memo[i + 1][cnv(X[i])] += 1

print(memo[N][MAX_I//2])
