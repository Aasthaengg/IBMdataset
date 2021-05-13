import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    A, B = [int(x) for x in input().split()]

    if A >= 1:
        print("Positive")
    elif A * B <= 0:
        print("Zero")
    else:
        if (abs(B) - abs(A) + 1) % 2 == 1:
            print("Negative")
        else:
            print("Positive")

    

if __name__ == '__main__':
    main()

