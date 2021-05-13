import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = f_inf
    for y in range(-100, 101):
        cost = 0
        for i in range(n):
            cost += pow(abs(A[i] - y), 2)
        res = min(res, cost)
    print(res)


if __name__ == '__main__':
    resolve()
