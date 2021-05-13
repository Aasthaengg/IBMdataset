def resolve():
    n, m = map(int, input().split())

    num_balls = [1] * n
    red_prov = [False] * n
    red_prov[0] = True

    for _ in range(m):
        x, y = map(lambda x: int(x) - 1, input().split())

        # リストnum_ballsを更新
        num_balls[x] -= 1
        num_balls[y] += 1

        # リストred_provを更新
        if red_prov[x]:
            red_prov[y] = True

        if num_balls[x] == 0:
            red_prov[x] = False

    print(sum(red_prov))
    
resolve()