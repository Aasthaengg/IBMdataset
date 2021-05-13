def solve(n, a):
    res, total = 0, 0
    for x in a:
        if x == 0:
            res += total // 2
            total = 0
        else:
            total += x
    return res + total // 2

n = int(input())
a = [int(input()) for i in range(n)]
print(solve(n, a))