import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]
    XY = [[int(x) for x in input().split()] for _ in range(M)]
    ans = [0] * (N + 1)
    ans[1] = 1
    cnt = [1] * (N + 1)
    for x, y in XY:
        if ans[x] == 1:
            ans[y] = 1
        if cnt[x] == 1:
            ans[x] = 0
        cnt[x] -= 1
        cnt[y] += 1

    print(sum(ans))


if __name__ == '__main__':
    main()
