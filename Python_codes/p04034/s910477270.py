import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    x = [0] * M
    y = [0] * M
    for i in range(M):
        x[i], y[i] = map(int, input().split())

    ball = [1] * N
    exist = [0] * N
    exist[0] = 1
    for a, b in zip(x, y):
        ball[a-1] -= 1
        ball[b-1] += 1
        if exist[a-1] == 1:
            exist[a-1] = 1 if ball[a-1] > 0 else 0
            exist[b-1] = 1

    ans = sum(exist)
    print(ans)


if __name__ == "__main__":
    main()
