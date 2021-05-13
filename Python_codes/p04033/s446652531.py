import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    def main():
        a, b = map(int, input().split())
        if a == 0 or b == 0:
            return 'Zero'
        elif a > 0:
            return 'Positive'
        else:
            if b<0:
                if (b-a)%2==0:
                    return 'Negative'
                else:
                    return 'Positive'
            else:
                return 'Zero'
    print(main())





resolve()