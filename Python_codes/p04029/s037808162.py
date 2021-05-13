import sys

input = sys.stdin.readline


def main():
    N = int(input())
    ans = N * (N+1) // 2
    print(ans)


if __name__ == "__main__":
    main()
