import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N,M,*xy = map(int, read().split())

    check = [False] * N
    check[0] = True
    num = [1] * N

    for x, y in zip(*[iter(xy)]*2):
        num[x-1] -= 1
        num[y-1] += 1
        if check[x-1]:
            check[y-1] = True
        if num[x-1] == 0:
            check[x-1] = False

    ans = sum(check)
    print(ans)


if __name__ == "__main__":
    main()
