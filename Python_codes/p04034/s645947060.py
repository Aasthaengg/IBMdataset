def main():
    n,m = map(int,input().split())
    box = [1] * n
    red = [0] * n
    red[0] += 1
    op = [list(map(int,input().split())) for _ in range(m)]
    for o in op:
        x, y = o[0]-1, o[1]-1
        if box[x] < 1:
            continue
        box[x] -= 1
        if red[x] > 0:
            red[y] = 1
        if box[x] == 0:
            red[x] = 0
        box[y] += 1
    print(sum(red))

if __name__ == "__main__":
    main()