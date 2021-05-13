import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    N, L = input_int_list()
    S = []
    for _ in range(N):
        S.append(input())
    S = sorted(S)
    print("".join(S))

    return


if __name__ == "__main__":
    main()
