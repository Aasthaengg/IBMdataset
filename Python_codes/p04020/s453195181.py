import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    n = int(input())
    A = [int(input()) for i in range(n)]

    ans = 0
    seq_cnt = 0
    for i in range(n):
        if A[i] != 0:
            seq_cnt += A[i]
        else:
            ans += seq_cnt // 2
            seq_cnt = 0
    ans += seq_cnt // 2

    print(ans)


resolve()