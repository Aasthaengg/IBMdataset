# https://atcoder.jp/contests/abc043/tasks/abc043_b

import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    S = input()
    ans = []
    for s in S:
        if s != "B":
            ans.append(s)
        else:
            if ans:
                ans.pop()
    print("".join(ans))

    return


if __name__ == "__main__":
    main()
