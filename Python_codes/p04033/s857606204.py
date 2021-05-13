mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    a, b = map(int, input().split())
    if a * b <= 0:
        print("Zero")
    else:
        if a > 0:
            print("Positive")
        else:
            if (b - a) & 1:
                print("Positive")
            else:
                print("Negative")


if __name__ == '__main__':
    main()
