def operate(x, y):
    if is_red[x]:
        is_red[y] = True
        if num_ball[x] == 1:
            is_red[x] = False
    num_ball[x] -= 1
    num_ball[y] += 1


if __name__ == "__main__":

    N, M = [int(x) for x in input().split(" ")]
    num_ball = [1 for _ in range(N)]
    is_red = [True] + [False for _ in range(N - 1)]

    for _ in range(M):
        x, y = [int(x) for x in input().split(" ")]
        x, y = x - 1, y - 1
        operate(x, y)
    print(sum(is_red))