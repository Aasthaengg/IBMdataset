def solve():
    def recur(i, n, total):
        # print("i, n, total", i, n, total)

        if not TABLE[i][n][total] == -1:
            return TABLE[i][n][total]

        if not i < N:
            if n > 0 and total == A * n:
                TABLE[i][n][total] = 1
                return TABLE[i][n][total]

            TABLE[i][n][total] = 0
            return TABLE[i][n][total]

        ans1 = recur(i + 1, n, total)
        ans2 = recur(i + 1, n + 1, total + XS[i])

        # print(ans1, ans2)

        TABLE[i][n][total] = ans1 + ans2
        return TABLE[i][n][total]

    N, A = tuple(map(int, input().split()))
    XS = tuple(map(int, input().split()))

    TABLE = []
    for _ in range(N + 1):
        lines = [[-1 for x in range(N * 50 + 1)] for y in range(N + 1)]
        TABLE.append(lines)

    return recur(0, 0, 0)


if __name__ == '__main__':
    print(solve())
