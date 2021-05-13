def main():
    N, M = (int(_) for _ in input().split())
    haco = [1] * (N+1)
    # 0:空, 1:白のみ取り出せる, 2:赤のみ, 3:どっちもあり得る
    cc = [1] * (N+1)
    haco[1] = 2
    for i in range(M):
        x, y = (int(_) for _ in input().split())
        cc[x] -= 1
        cc[y] += 1
        if haco[x] == 1:
            haco[y] = 3 if haco[y] in (2, 3) else 1
        elif haco[x] == 2:
            haco[y] = 2 if haco[y] == 0 else 3
        else:
            haco[y] = 3
        if cc[x] == 0: haco[x] = 0
    output = 0
    for i in range(1, N+1):
        if haco[i] in (2, 3):
            output += 1
    print(output)
    return

if __name__ == '__main__':
    main()
