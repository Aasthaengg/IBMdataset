import sys

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())

    if b < 0:
        if (b - a) % 2 == 0:
            ans = "Negative"
        else:
            ans = "Positive"
    elif a <= 0 <= b:
        ans = "Zero"
    else:
        ans = "Positive"

    print(ans)


if __name__ == "__main__":
    main()
