import sys
input = sys.stdin.readline


def read():
    a, b = map(int, input().strip().split())
    return a, b


def solve(a, b):
    if a <= 0 and 0 <= b:
        return "Zero"
    minus = 0
    if b < 0:
        minus = abs(b - a) + 1
    return "Positive" if minus % 2 == 0 else "Negative"


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
