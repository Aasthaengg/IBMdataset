import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    L = [int(x) for x in input().split()]

    L.sort()
    ans = 0
    for i in range(0, N * 2, 2):
        ans += L[i]

    print(ans)




if __name__ == '__main__':
    main()
