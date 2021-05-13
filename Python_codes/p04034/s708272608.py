from sys import stdin


def main():
    input = lambda: stdin.readline()[:-1]
    N, M = map(int, input().split())
    XY = [tuple(map(int, input().split())) for _ in [0] * M]

    box = [1] * (N + 1)
    red = [0] * (N + 1)
    box[0], red[1] = 0, 1
    for x, y in XY:
        box[x] -= 1
        box[y] += 1
        if red[x]:
            red[y] = 1
        if not box[x]:
            red[x] = 0
    print(sum(red))


main()
