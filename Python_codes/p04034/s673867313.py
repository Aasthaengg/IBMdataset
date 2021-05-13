import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, m = map(int, input().split())
    balls = [1] * (n + 1)
    posib = [0] * (n + 1)
    posib[1] = 1
    m = map(int, read().split())
    ab = zip(m, m)
    for x, y in ab:
        if posib[x]:
            posib[y] = 1
        balls[y] += 1
        balls[x] -= 1
        if not balls[x]:
            posib[x] = 0
    r = sum(posib)
    print(r)

if __name__ == '__main__':
    main()