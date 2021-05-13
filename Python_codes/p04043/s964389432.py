import sys
import math
import collections
import heapq

def set_debug(debug_mode=False):
    if debug_mode:
        fin = open('input.txt', 'r')
        sys.stdin = fin


def int_input():
    return list(map(int, input().split()))


if __name__ == '__main__':
    # set_debug(True)

    # t = int(input())
    t = 1

    for ti in range(1, t + 1):
        a, b, c = int_input()

        if (a == b == 5 and c == 7) or (a == c == 5 and b == 7) or (b == c ==5 and a == 7):
            print('YES')
        else:
            print('NO')

